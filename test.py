import sys
import os
from huggingface_hub import snapshot_download

REPO_ID = "Qwen/Qwen2.5-VL-3B-Instruct"
print(f"Downloading {REPO_ID}...")

try:
    path = snapshot_download(repo_id=REPO_ID, max_workers=1)
    print(f"Downloaded {REPO_ID} -> {path}")
except Exception as e:
    print(f"Download failed: {e}", file=sys.stderr)
    sys.exit(1)
