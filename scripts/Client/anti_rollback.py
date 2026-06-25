from pathlib import Path
import json
from logger import logger

BASE_DIR = Path(__file__).resolve().parent
DOWNLOAD_DIR = BASE_DIR / "downloads"

# for dev
CURRENT_VERSION_PATH = (
    BASE_DIR.parent.parent
    / "firmware"
    / "version.json"
)

# for client 
# CURRENT_VERSION_PATH = (
#     BASE_DIR.parent.parent
#     /"Python"
#     /"Client OTA Server (Cybersecurity)"
#     / "installed_version.json"
# )

DOWNLOADED_VERSION_PATH = (
    DOWNLOAD_DIR
    / "version.json"
)


def parse_version(version):
    return tuple(
        map(
            int,
            version.split(".")
        )
    )


def anti_rollback():
    logger.info(
        "Performing Anti Rollback Check"
    )
    with open(
        CURRENT_VERSION_PATH,
        "r"
    ) as file:
        current_data = json.load(file)

    with open(
        DOWNLOADED_VERSION_PATH,
        "r"
    ) as file:
        incoming_data = json.load(file)

    current_version = parse_version(
        current_data["version"]
    )
    incoming_version = parse_version(
        incoming_data["version"]
    )

    logger.info(
        f"Current Version : {current_data['version']}"
    )
    logger.info(
        f"Incoming Version : {incoming_data['version']}"
    )

    print(
        f"Current Version : {current_data['version']}"
    )
    print(
        f"Incoming Version : {incoming_data['version']}"
    )

    if incoming_version < current_version:
        logger.warning(
            "ROLLBACK DETECTED"
        )
        print(
            "ROLLBACK DETECTED"
        )
        return False
    logger.info(
        "Anti Rollback Check PASSED"
    )
    print(
        "UPDATE ALLOWED"
    )
    return True