import sys
import os

os.environ["HF_XET_NUM_CONCURRENT_RANGE_GETS"] = "16"
from huggingface_hub import snapshot_download

REPO_ID = "Qwen/Qwen2.5-VL-3B-Instruct"
print(f"Downloading {REPO_ID}...")

try:
    path = snapshot_download(repo_id=REPO_ID)
    print(f"Downloaded {REPO_ID} -> {path}")
except Exception as e:
    print(f"Download failed: {e}", file=sys.stderr)
    sys.exit(1)
