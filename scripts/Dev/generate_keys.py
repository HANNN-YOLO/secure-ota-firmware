from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
KEYS_DIR = BASE_DIR / "keys"

PRIVATE_KEY_PATH = KEYS_DIR / "private_key.pem"
PUBLIC_KEY_PATH = KEYS_DIR / "public_key.pem"


# Generate ECDSA Private Key
private_key = ec.generate_private_key(
    ec.SECP256R1()
)

# Convert Private Key Object -> PEM Bytes
private_bytes = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

with open(PRIVATE_KEY_PATH, "wb") as f:
    f.write(private_bytes)

# Generate Public Key from Private Key
public_key = private_key.public_key()

# Convert Public Key Object -> PEM Bytes
public_bytes = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

with open(PUBLIC_KEY_PATH, "wb") as f:
    f.write(public_bytes)

print("Private Key saved successfully!")
print("Public Key saved successfully!")