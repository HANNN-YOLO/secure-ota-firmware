from pathlib import Path
import json

from logger import logger

BASE_DIR = Path(__file__).resolve().parent
DOWNLOAD_DIR = BASE_DIR / "downloads"

INSTALLED_VERSION_PATH = (
    BASE_DIR / "installed_version.json"
)
DOWNLOADED_VERSION_PATH = (
    DOWNLOAD_DIR / "version.json"
)

def update_installed_version():
    with open(
        DOWNLOADED_VERSION_PATH,
        "r"
    ) as file:
        downloaded_data = json.load(file)
    with open(
        INSTALLED_VERSION_PATH,
        "w"
    ) as file:
        json.dump(
            downloaded_data,
            file,
            indent=4
        )
    logger.info(
        f"Installed Version Updated -> "
        f"{downloaded_data['version']}"
    )
    print(
        f"Installed Version Updated -> "
        f"{downloaded_data['version']}"
    )
    return True