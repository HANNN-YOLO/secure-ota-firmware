import hashlib
from pathlib import Path

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec

from logger import logger

BASE_DIR = Path(__file__).resolve().parent

DOWNLOAD_DIR = BASE_DIR / "downloads"

VERSION_PATH = DOWNLOAD_DIR / "version.json"
VERSION_SIGNATURE_PATH = DOWNLOAD_DIR / "version.sig"

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

def verify_signature_version():
    logger.info(
        "Verifying Version Signature"
    )
    try:
        version_data = VERSION_PATH.read_bytes()
        version_hash = hashlib.sha256(
            version_data
        ).digest()
        signature = (
            VERSION_SIGNATURE_PATH.read_bytes()
        )
        with open(
            PUBLIC_KEY_PATH,
            "rb"
        ) as file:
            public_key = (
                serialization.load_pem_public_key(
                    file.read()
                )
            )
        public_key.verify(
            signature,
            version_hash,
            ec.ECDSA(
                hashes.SHA256()
            )
        )
        logger.info(
            "Version Signature VALID"
        )
        print(
            "Version Signature VALID"
        )
        return True
    except InvalidSignature:
        logger.error(
            "Version Signature INVALID"
        )
        print(
            "Version Signature INVALID"
        )
        return False