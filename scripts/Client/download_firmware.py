from pathlib import Path
import requests
from logger import logger
from anti_rollback import anti_rollback
from verify_hash import verify_hash
from verify_signature_version import verify_signature_version
from verify_signature_firmware import verify_signature_firmware
from update_installed_version import update_installed_version

BASE_DIR = Path(__file__).resolve().parent
DOWNLOAD_DIR = BASE_DIR / "downloads"
DOWNLOAD_DIR.mkdir(
    exist_ok=True
)

# ipv4 for flask dev, client and docker client 
SERVER_URL = "http://10.136.176.226:8080"

# localhost for docker dev 
# SERVER_URL = "http://localhost:8080"

def download_file(
    endpoint,
    filename
):
    url = (
        f"{SERVER_URL}/{endpoint}"
    )
    logger.info(
        f"Downloading {filename}"
    )
    try:
        response = requests.get(
            url,
            timeout=10
        )
        response.raise_for_status()
        file_path = (
            DOWNLOAD_DIR / filename
        )
        with open(
            file_path,
            "wb"
        ) as file:
            file.write(
                response.content
            )
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
        return False


def main():
    logger.info(
        "OTA Client Started"
    )
    print(
        "\n=== VERSION VALIDATION ==="
    )
    version_ok = download_file(
        "version.json",
        "version.json"
    )
    version_signature_ok = download_file(
        "version.sig",
        "version.sig"
    )
    if not (
        version_ok and
        version_signature_ok
    ):
        logger.error(
            "Version Download Failed"
        )
        return
    if not verify_signature_version():
        logger.error(
            "Version Verification Failed"
        )
        return
    if not anti_rollback():
        logger.warning(
            "Rollback Attack Detected"
        )
        print(
            "Update Rejected"
        )
        return
    logger.info(
        "Version Validation Passed"
    )
    print(
        "\n=== FIRMWARE VALIDATION ==="
    )
    firmware_ok = download_file(
        "firmware.bin",
        "firmware.bin"
    )
    firmware_hash_ok = download_file(
        "firmware_hash.md",
        "firmware_hash.md"
    )
    firmware_signature_ok = download_file(
        "firmware.sig",
        "firmware.sig"
    )
    if not (
        firmware_ok and
        firmware_hash_ok and
        firmware_signature_ok
    ):
        logger.error(
            "Firmware Download Failed"
        )
        return
    if not verify_hash():
        logger.error(
            "Firmware Hash Verification Failed"
        )
        return
    if not verify_signature_firmware():
        logger.error(
            "Firmware Signature Verification Failed"
        )
        return
    logger.info(
        "Firmware Verification Passed"
    )
    update_installed_version()
    logger.info(
        "Firmware Ready To Install"
    )
    print(
        "\nFirmware Ready To Install"
    )

if __name__ == "__main__":
    main()