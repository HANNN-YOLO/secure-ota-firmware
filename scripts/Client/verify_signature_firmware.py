# from pathlib import Path
# from cryptography.exceptions import InvalidSignature
# from cryptography.hazmat.primitives import hashes
# from cryptography.hazmat.primitives import serialization
# from cryptography.hazmat.primitives.asymmetric import ec
# from logger import logger

# BASE_DIR = Path(__file__).resolve().parent

# # ini untuk client
# # BASE_DIR2 = Path(__file__).resolve().parent.parent

# # ini untuk dev
# BASE_DIR1 = Path(__file__).resolve().parent.parent.parent

# FIRMWARE_PATH = BASE_DIR / "downloads" / "firmware.bin"
# SIGNATURE_PATH = BASE_DIR / "downloads" / "signature.sig"

# # ini untuk client
# # PUBLIC_KEY_PATH = BASE_DIR / "public_key.pem"

# # ini untuk dev
# PUBLIC_KEY_PATH = BASE_DIR1 / "keys" / "public_key.pem"


# def verify_signature():
#     logger.info(f"Firmware Path : {FIRMWARE_PATH}")
#     logger.info(f"Signature Path : {SIGNATURE_PATH}")
#     logger.info(f"Public Key Path : {PUBLIC_KEY_PATH}")
#     firmware_data = FIRMWARE_PATH.read_bytes()
#     signature = SIGNATURE_PATH.read_bytes()
#     with open(PUBLIC_KEY_PATH, "rb") as file:
#         public_key = serialization.load_pem_public_key(
#             file.read()
#         )
#         logger.info(
#         "Verify Signature Started"
#     )
#     try:
#         public_key.verify(
#             signature,
#             firmware_data,
#             ec.ECDSA(hashes.SHA256())
#         )
#         logger.info(
#             "Digital Signature successfull"
#         )
#         print("Signature VALID")
#         return True
#     except InvalidSignature:
#         logger.info(
#             "Digital Signature Failed"
#         )
#         print("Signature INVALID")
#         return False

# if __name__ == "__main__":
#     verify_signature()
import hashlib
from pathlib import Path

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.exceptions import InvalidSignature

from logger import logger

BASE_DIR = Path(__file__).resolve().parent

DOWNLOAD_DIR = BASE_DIR / "downloads"

FIRMWARE_PATH = DOWNLOAD_DIR / "firmware.bin"
SIGNATURE_PATH = DOWNLOAD_DIR / "firmware.sig"

# for dev
PUBLIC_KEY_PATH = (
    BASE_DIR.parent.parent
    / "keys"
    / "public_key.pem"
)

# for client
# PUBLIC_KEY_PATH = (
#     BASE_DIR.parent.parent
#     /"Python"
#     /"Client OTA Server (Cybersecurity)"
#     / "public_key.pem"
# )

def verify_signature_firmware():
    logger.info(
        "Verify Signature Started"
    )
    logger.info(
        f"Firmware Path : {FIRMWARE_PATH}"
    )
    logger.info(
        f"Signature Path : {SIGNATURE_PATH}"
    )
    logger.info(
        f"Public Key Path : {PUBLIC_KEY_PATH}"
    )
    firmware_data = FIRMWARE_PATH.read_bytes()
    signature = SIGNATURE_PATH.read_bytes()
    logger.info(
        f"Firmware Size : {len(firmware_data)} bytes"
    )
    logger.info(
        f"Signature Size : {len(signature)} bytes"
    )
    with open(PUBLIC_KEY_PATH, "rb") as file:
        public_key = serialization.load_pem_public_key(
            file.read()
        )
    logger.info(
        "Public Key Loaded Successfully"
    )
    try:
        logger.info(
            "Verifying Signature Against Firmware"
        )

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

        # step 3 - Load Verify signature againts firmware
        public_key.verify(
            signature,
            firmware_hash,
            ec.ECDSA(hashes.SHA256())
        )
        logger.info(
            "Digital Signature Successful"
        )
        print(
            "Signature VALID"
        )
        return True
    except InvalidSignature:
        logger.error(
            "Digital Signature Failed"
        )
        print(
            "Signature INVALID"
        )
        return False