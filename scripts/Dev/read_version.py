from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent.parent.parent

VERSION_FILE = BASE_DIR / "firmware" / "version.json"

with open(VERSION_FILE, "r") as file:
    data = json.load(file)

print("Firmware Version:", data["version"])