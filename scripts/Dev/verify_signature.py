# import hashlib
# from cryptography.hazmat.primitives import hashes
# from cryptography.hazmat.primitives import serialization
# from cryptography.hazmat.primitives.asymmetric import ec
# from cryptography.exceptions import InvalidSignature


# # STEP 1 - Load firmware
# with open("../firmware/firmware.bin", "rb") as firmware_file:
#     firmware_data = firmware_file.read()

# print("Firmware Loaded Successfully")

# firmware_hash = hashlib.sha256(firmware_data).digest()

# print("Firmware Hash Generated Successfully")


# # STEP 2 - Load signature
# with open("../Output/signature.sig", "rb") as sig_file:
#     signature = sig_file.read()

# print("Signature Loaded Successfully")


# # STEP 3 - Load public key
# with open("../keys/public_key.pem", "rb") as key_file:
#     public_key = serialization.load_pem_public_key(
#         key_file.read()
#     )

# print("Public Key Loaded Successfully")


# # STEP 4 - Verify Signature
# try:
#     public_key.verify(
#         signature,
#         firmware_hash,
#         ec.ECDSA(hashes.SHA256())
#     )

#     print("\n[VALID]")
#     print("Firmware verification successful.")
#     print("Firmware is authentic and unchanged.")

# except InvalidSignature:

#     print("\n[INVALID]")
#     print("Firmware verification failed.")
#     print("Firmware may have been modified.")

import hashlib

from pathlib import Path

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.exceptions import InvalidSignature


BASE_DIR = Path(__file__).resolve().parent.parent.parent

FIRMWARE_PATH = BASE_DIR / "firmware" / "firmware.bin"
PUBLIC_KEY_PATH = BASE_DIR / "keys" / "public_key.pem"
SIGNATURE_PATH = BASE_DIR / "output" / "signature.sig"


# STEP 1 - Load firmware
with open(FIRMWARE_PATH, "rb") as firmware_file:
    firmware_data = firmware_file.read()

print("Firmware Loaded Successfully")

firmware_hash = hashlib.sha256(firmware_data).digest()

print("Firmware Hash Generated Successfully")


# STEP 2 - Load signature
with open(SIGNATURE_PATH, "rb") as sig_file:
    signature = sig_file.read()

print("Signature Loaded Successfully")


# STEP 3 - Load public key
with open(PUBLIC_KEY_PATH, "rb") as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read()
    )

print("Public Key Loaded Successfully")


# STEP 4 - Verify Signature
try:
    public_key.verify(
        signature,
        firmware_hash,
        ec.ECDSA(hashes.SHA256())
    )

    print("\n[VALID]")
    print("Firmware verification successful.")
    print("Firmware is authentic and unchanged.")

except InvalidSignature:

    print("\n[INVALID]")
    print("Firmware verification failed.")
    print("Firmware may have been modified.")