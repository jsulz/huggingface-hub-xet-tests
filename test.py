
import sys
from huggingface_hub import snapshot_download

REPO_ID = "Qwen/Qwen2.5-Omni-7B"

try:
    path = snapshot_download(repo_id=REPO_ID)
    print(f"Downloaded {REPO_ID} -> {path}")
except Exception as e:
    print(f"Download failed: {e}", file=sys.stderr)
    sys.exit(1)