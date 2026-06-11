import argparse
import socket
from oqs import KeyEncapsulation
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os

parser = argparse.ArgumentParser(description="Intercambio de claves ML-KEM-512 y cifrado (Cliente)")
parser.add_argument("-g", "--gateway", help="Dirección IP del gateway")
parser.add_argument("-t", "--target", help="Dirección IP del target")
parser.add_argument("-m", "--message", default="¡Hola, este es un mensaje secreto!", help="Mensaje a cifrar")
args = parser.parse_args()

print(f"Gateway: {args.gateway}, Target: {args.target}")

kem = KeyEncapsulation("ML-KEM-512")
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((args.target, 12345))
        public_key = s.recv(kem.length_public_key)
        print("Recibido public_key (%d bytes): %s" % (len(public_key), public_key.hex()))
        ciphertext, shared_secret = kem.encap_secret(public_key)
        print("Enviando ciphertext (%d bytes): %s" % (len(ciphertext), ciphertext.hex()))
        s.sendall(ciphertext)
        print("Enviado ciphertext al target")

        # Usa shared_secret directamente (sin PBKDF2 para compatibilidad)
        aes_key = shared_secret
        aesgcm = AESGCM(aes_key)
        message = args.message.encode('utf-8')
        nonce = os.urandom(12)
        encrypted_message = aesgcm.encrypt(nonce, message, None)
        print("Enviando nonce (%d bytes): %s, encrypted_message (%d bytes): %s" % (len(nonce), nonce.hex(), len(encrypted_message), encrypted_message.hex()))
        s.sendall(nonce + encrypted_message)
        print("Enviado mensaje cifrado al target")

    print("Shared secret (gateway):", shared_secret.hex())
except ConnectionRefusedError:
    print(f"Error: No se pudo conectar al target {args.target}:12345.")
except Exception as e:
    print(f"Error: {e}")
