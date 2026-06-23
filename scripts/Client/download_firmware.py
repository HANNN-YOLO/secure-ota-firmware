from pathlib import Path
import requests
from logger import logger
from verify_hash import verify_hash
from verify_signature import verify_signature

BASE_DIR = Path(__file__).resolve().parent

DOWNLOAD_DIR = BASE_DIR / "downloads"
DOWNLOAD_DIR.mkdir(exist_ok=True)

# ipv4 for flask dev, client and docker client
SERVER_URL = "http://10.136.176.226:8080"

# localhost for docker dev
# SERVER_URL = "http://localhost:8080"

def download_file(endpoint, filename):
    url = f"{SERVER_URL}/{endpoint}"
    logger.info(f"Starting download {filename}")
    try:
        response = requests.get(
            url,
            timeout=10
        )
        response.raise_for_status()
        file_path = DOWNLOAD_DIR / filename
        with open(file_path, "wb") as file:
            file.write(response.content)
        logger.info(
            f"{filename} downloaded successfully"
        )
        print(
            f"{filename} downloaded successfully"
        )
        return True
    except Exception as error:
        logger.error(
            f"Download failed {filename}: {error}"
        )
        print(
            f"Download failed: {filename}"
        )
        return False


def main():
    logger.info(
        "OTA client started"
    )
    firmware_ok = download_file(
        "firmware.bin",
        "firmware.bin"
    )
    signature_ok = download_file(
        "signature.sig",
        "signature.sig"
    )
    hash_result_Ok = download_file(
        "hash_result.md",
        "hash_result.md",
    )
    if firmware_ok and signature_ok and hash_result_Ok:
        logger.info(
            "All files downloaded successfully"
        )
        print(
            "All files downloaded successfully"
        )
        verify_hash()
        verify_signature()
    else:
        logger.error(
            "Download process failed"
        )
        print(
            "Download process failed"
        )

if __name__ == "__main__":
    main()