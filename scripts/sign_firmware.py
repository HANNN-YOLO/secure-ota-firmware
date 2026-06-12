import hashlib

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec


# STEP 1 - Read firmware file
with open("../firmware/firmware.bin", "rb") as file:
    firmware_data = file.read()


# STEP 2 - Calculate SHA256 hash
firmware_hash = hashlib.sha256(firmware_data).digest()

print("Firmware Hash Generated Successfully")


# STEP 3 - Load private key
with open("../keys/private_key.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None
    )

print("Private Key Loaded Successfully")


# STEP 4 - Sign hash using ECDSA
signature = private_key.sign(
    firmware_hash,
    ec.ECDSA(hashes.SHA256())
)

print("Digital Signature Generated Successfully")


# STEP 5 - Save signature
with open("../Output/signature.sig", "wb") as sig_file:
    sig_file.write(signature)

print("Signature saved to Output/signature.sig")