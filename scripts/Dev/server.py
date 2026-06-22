from pathlib import Path
from flask import Flask, send_file

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent.parent.parent

FIRMWARE_PATH = BASE_DIR / "firmware" / "firmware.bin"
SIGNATURE_PATH = BASE_DIR / "output" / "signature.sig"


@app.route("/firmware.bin")
def download_firmware():
    return send_file(
        FIRMWARE_PATH,
        as_attachment=True
    )


@app.route("/signature.sig")
def download_signature():
    return send_file(
        SIGNATURE_PATH,
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8080
    )