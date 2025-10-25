from pathlib import Path
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get project root
PROJECT_ROOT = Path(os.getenv("PROJECT_ROOT", Path(__file__).resolve().parents[1]))

# Define paths
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA = DATA_DIR / "raw" / "AmesHousing.csv"
PROCESSED_DIR = DATA_DIR / "processed"
MODELS_DIR = PROJECT_ROOT / "models"

# Create missing folders automatically
for path in [PROCESSED_DIR, MODELS_DIR]:
    path.mkdir(parents=True, exist_ok=True)
