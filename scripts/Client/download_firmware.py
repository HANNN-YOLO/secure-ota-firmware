from pathlib import Path
import requests

BASE_DIR = Path(__file__).resolve().parent
DOWNLOAD_DIR = BASE_DIR / "downloads"

DOWNLOAD_DIR.mkdir(exist_ok=True)

SERVER_URL = "http://10.136.176.226:8080"


def download_file(endpoint, filename):
    url = f"{SERVER_URL}/{endpoint}"

    print(f"Downloading {filename}...")

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    file_path = DOWNLOAD_DIR / filename

    with open(file_path, "wb") as file:
        file.write(response.content)

    print(f"{filename} downloaded successfully")


def main():
    download_file("firmware.bin", "firmware.bin")
    download_file("signature.sig", "signature.sig")

    print("All files downloaded successfully")

if __name__ == "__main__":
    main()