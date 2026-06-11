import argparse
from utils.crypto import decrypt_password

parser = argparse.ArgumentParser(description="Descifra una contraseña post-cuántica usando ML-KEM-512 y AES-GCM.")
parser.add_argument('--encrypted', required=True, help='Ruta al archivo con la contraseña cifrada (binario)')
parser.add_argument('--seckey', required=True, help='Ruta al archivo con la clave secreta (binario)')
parser.add_argument('--kem', required=True, help='Ruta al archivo con el KEM ciphertext (binario)')
args = parser.parse_args()

with open(args.encrypted, 'rb') as f:
    encrypted_password = f.read()
with open(args.seckey, 'rb') as f:
    secret_key = f.read()
with open(args.kem, 'rb') as f:
    kem_ciphertext = f.read()

try:
    password = decrypt_password(encrypted_password, secret_key, kem_ciphertext)
    print(password)
except Exception as e:
    print(f'ERROR: {e}', flush=True)
    exit(1) 