import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

LOG_FILE = BASE_DIR / "verification.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)