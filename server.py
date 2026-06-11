import socket
from oqs import KeyEncapsulation
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

kem = KeyEncapsulation("ML-KEM-512")
keys = kem.generate_keypair()
public_key = keys[:kem.length_public_key]
secret_key = keys[kem.length_public_key:kem.length_public_key + kem.length_secret_key]
print("Public key size: %d, Ciphertext size: %d" % (kem.length_public_key, kem.length_ciphertext))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('0.0.0.0', 12345))
    s.listen()
    print("Servidor escuchando en 0.0.0.0:12345...")
    conn, addr = s.accept()
    with conn:
        print(f"Conexión establecida desde {addr}")
        print("Enviando public_key (%d bytes): %s" % (len(public_key), public_key.hex()))
        conn.sendall(public_key)
        data = conn.recv(kem.length_ciphertext)
        print("Recibido ciphertext (%d bytes): %s" % (len(data), data.hex()))
        ciphertext = data
        shared_secret = kem.decap_secret(ciphertext)
        print("Shared secret (target):", shared_secret.hex())

        # Usa shared_secret directamente (sin PBKDF2)
        aes_key = shared_secret
        aesgcm = AESGCM(aes_key)

        data = conn.recv(12 + 1024)
        nonce = data[:12]
        encrypted_message = data[12:]
        print("Recibido nonce (%d bytes): %s, encrypted_message (%d bytes): %s" % (len(nonce), nonce.hex(), len(encrypted_message), encrypted_message.hex()))
        try:
            decrypted_message = aesgcm.decrypt(nonce, encrypted_message, None)
            print("Mensaje descifrado:", decrypted_message.decode('utf-8'))
        except Exception as e:
            print("Error al descifrar:", e)
