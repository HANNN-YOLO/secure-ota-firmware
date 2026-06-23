from pathlib import Path
import hashlib
from logger import logger

BASE_DIR = Path(__file__).resolve().parent

DOWNLOAD_DIR = BASE_DIR / "downloads"

FIRMWARE_PATH = DOWNLOAD_DIR / "firmware.bin"
HASH_PATH = DOWNLOAD_DIR / "hash_result.md"

def calculate_sha256(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            sha256.update(chunk)
    return sha256.hexdigest()

def read_server_hash():
    try:
        with open(HASH_PATH, "r") as file:
            content = file.read().strip()
            if ":" in content:
                return content.split(":", 1)[1].strip()
            if "=" in content:
                return content.split("=", 1)[1].strip()
            return content
    except Exception as error:
        logger.error(
            f"Failed reading server hash: {error}"
        )
        return None

def verify_hash():
    logger.info(
        "Hash verification started"
    )
    try:
        local_hash = calculate_sha256(
            FIRMWARE_PATH
        )
        server_hash = read_server_hash()
        if not server_hash:
            logger.error(
                "Server hash not found"
            )
            return False
        logger.info(
            f"Local Hash : {local_hash}"
        )
        logger.info(
            f"Server Hash : {server_hash}"
        )
        if local_hash == server_hash:
            logger.info(
                "Hash verification successful"
            )
            print(
                "Firmware hash VALID"
            )
            return True
        logger.error(
            "Hash verification failed"
        )
        print(
            "Firmware hash INVALID"
        )
        return False
    except Exception as error:
        logger.error(
            f"Verification error: {error}"
        )
        return False

if __name__ == "__main__":
    verify_hash()