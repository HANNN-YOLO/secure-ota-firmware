import hashlib

with open("firmware/dumy_firmware.bin", "rb") as file:
    data = file.read()

sha256_hash = hashlib.sha256(data).hexdigest()

print("SHA256:", sha256_hash)