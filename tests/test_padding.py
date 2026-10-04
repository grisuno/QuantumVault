"""Contract tests for fixed-bucket padding (QV-PAD-1) and its enforcement."""

from __future__ import annotations

import base64

import pytest

from controllers.file import FileController
from controllers.message import MessageController
from utils import padding
from utils.padding import (
    GCM_OVERHEAD_BYTES,
    LENGTH_PREFIX_BYTES,
    PaddingConfig,
    PaddingError,
    bucket_for,
    cached_tables,
    config_from_env,
    is_allowed_ciphertext_len,
    pad,
    unpad,
)


def test_pad_roundtrip_message_sizes() -> None:
    for size in (0, 1, 100, 508, 509, 1024 - LENGTH_PREFIX_BYTES, 5000):
        body = bytes(size)
        framed = pad(body, "message")
        assert unpad(framed, "message") == body


def test_pad_roundtrip_file_kind() -> None:
    body = b"f" * 70000
    assert unpad(pad(body, "file"), "file") == body


def test_bucket_boundaries() -> None:
    assert bucket_for(508, "message") == 512
    assert bucket_for(509, "message") == 1024
    assert bucket_for(0, "message") == 512


def test_pad_output_length_is_bucketed() -> None:
    assert len(pad(b"hi", "message")) == 512
    assert len(pad(b"hi", "file")) == 65536


def test_pad_uses_fresh_randomness() -> None:
    first = pad(b"same", "message")
    second = pad(b"same", "message")
    assert len(first) == len(second) == 512
    assert first != second


def test_pad_rejects_oversize() -> None:
    with pytest.raises(PaddingError):
        pad(bytes(65536), "message")


def test_unpad_rejects_non_bucket_length() -> None:
    with pytest.raises(PaddingError):
        unpad(bytes(100), "message")


def test_unpad_rejects_corrupt_prefix() -> None:
    framed = bytearray(pad(b"ok", "message"))
    framed[0] = 0xFF
    framed[1] = 0xFF
    with pytest.raises(PaddingError):
        unpad(bytes(framed), "message")


def test_unpad_rejects_wrong_kind() -> None:
    framed = pad(b"ok", "message")
    with pytest.raises(PaddingError):
        unpad(framed, "file")


def test_wire_lengths() -> None:
    assert is_allowed_ciphertext_len(512 + GCM_OVERHEAD_BYTES, "message")
    assert not is_allowed_ciphertext_len(513 + GCM_OVERHEAD_BYTES, "message")
    assert is_allowed_ciphertext_len(65536 + GCM_OVERHEAD_BYTES, "file")
    assert not is_allowed_ciphertext_len(10, "file")


def test_config_from_env_override(monkeypatch) -> None:
    monkeypatch.setenv("QV_PAD_MESSAGE_BUCKETS", "64,128")
    config = config_from_env()
    assert config.message_buckets == (64, 128)
    assert bucket_for(60, "message", config) == 64


def test_config_from_env_falls_back_on_garbage(monkeypatch) -> None:
    monkeypatch.setenv("QV_PAD_MESSAGE_BUCKETS", "nope")
    assert config_from_env().message_buckets == padding.DEFAULT_MESSAGE_BUCKETS


def test_cache_holds_tables_not_pad_bytes() -> None:
    config = PaddingConfig()
    assert cached_tables(config) is cached_tables(config)
    assert cached_tables(config)[0] == padding.DEFAULT_MESSAGE_BUCKETS


def test_message_controller_rejects_unpadded_envelope(app, tmp_path, monkeypatch) -> None:
    controller = MessageController(str(tmp_path))
    monkeypatch.setattr(controller.user_db, "get_user", lambda username: {"id": 1})
    raw = base64.b64encode(bytes(100)).decode("ascii")
    with app.test_request_context():
        assert controller.send_encrypted_message("a", "b", raw, "k1", "k2") is False


def test_message_controller_rejects_malformed_base64(app, tmp_path, monkeypatch) -> None:
    controller = MessageController(str(tmp_path))
    monkeypatch.setattr(controller.user_db, "get_user", lambda username: {"id": 1})
    with app.test_request_context():
        assert controller.send_encrypted_message("a", "b", "!!!", "k1", "k2") is False


def test_message_controller_accepts_bucketed_envelope(app, tmp_path, monkeypatch) -> None:
    controller = MessageController(str(tmp_path))
    monkeypatch.setattr(controller.user_db, "get_user", lambda username: {"id": 1})
    raw = base64.b64encode(bytes(512 + GCM_OVERHEAD_BYTES)).decode("ascii")
    with app.test_request_context():
        assert controller.send_encrypted_message("a", "b", raw, "k1", "k2") is True


class _FakeS3:
    def __init__(self) -> None:
        self.objects: dict[str, bytes] = {}

    def put_object(self, Bucket: str, Key: str, Body: bytes) -> None:
        self.objects[Key] = Body


class _FakeUpload:
    filename = "note.bin"

    def __init__(self, body: bytes) -> None:
        self._body = body

    def read(self) -> bytes:
        return self._body


def test_file_controller_rejects_unpadded_upload(app) -> None:
    controller = FileController("users", "bucket", _FakeS3())
    with app.test_request_context():
        assert controller.upload_encrypted_file("u", _FakeUpload(bytes(100)), b"fek") is False


def test_file_controller_accepts_bucketed_upload(app) -> None:
    s3 = _FakeS3()
    controller = FileController("users", "bucket", s3)
    body = bytes(65536 + GCM_OVERHEAD_BYTES)
    with app.test_request_context():
        assert controller.upload_encrypted_file("u", _FakeUpload(body), b"fek") is True
    assert s3.objects["users/u/files/encrypted/note.bin"] == body
