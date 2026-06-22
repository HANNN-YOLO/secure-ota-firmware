# import hashlib

# with open("firmware/firmware.bin", "rb") as file:
#     data = file.read()

# sha256_hash = hashlib.sha256(data).hexdigest()

# print("SHA256:", sha256_hash)

import hashlib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

FIRMWARE_PATH = BASE_DIR / "firmware" / "firmware.bin"

with open(FIRMWARE_PATH, "rb") as file:
    data = file.read()

sha256_hash = hashlib.sha256(data).hexdigest()

print("SHA256:", sha256_hash)