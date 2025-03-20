import os
from pathlib import Path

NIFTY50_URL="https://archives.nseindia.com/content/indices/ind_nifty50list.csv"
WORKING_DIRECTORY = Path(__file__).parent.parent
DATA_DIRECTORY = os.path.join(WORKING_DIRECTORY, "data")
RAW_DATA_DIRECTORY = os.path.join(DATA_DIRECTORY, "raw")
PROCESSED_DATA_DIRECTORY = os.path.join(DATA_DIRECTORY, "processed")
RESULTS_DIRECTORY = os.path.join(WORKING_DIRECTORY, "results")