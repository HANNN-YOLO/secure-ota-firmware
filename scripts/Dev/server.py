from pathlib import Path
from flask import Flask, send_file

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent.parent.parent

FIRMWARE_PATH = BASE_DIR / "firmware" / "firmware.bin"
FIRMWARE_HASH_PATH = BASE_DIR / "output" / "firmware_hash.md"
FIRMWARE_SIGNATURE_PATH = BASE_DIR / "output" / "firmware.sig"
VERSION_PATH = BASE_DIR / "firmware" / "version.json"
VERSION_SIGNATURE_PATH = BASE_DIR / "output" / "version.sig"

@app.route("/firmware.bin")
def download_firmware():
    return send_file(
        FIRMWARE_PATH,
        as_attachment=True
    )

@app.route("/firmware_hash.md")
def download_firmware_hash():
    return send_file(
        FIRMWARE_HASH_PATH,
        as_attachment=True
    )

@app.route("/firmware.sig")
def download_firmware_signature():
    return send_file(
        FIRMWARE_SIGNATURE_PATH,
        as_attachment=True
    )

@app.route("/version.json")
def download_version():
    return send_file(
        VERSION_PATH,
        as_attachment=True
    )

@app.route("/version.sig")
def download_version_signature():
    return send_file(
        VERSION_SIGNATURE_PATH,
        as_attachment=True
    )

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8080
    )