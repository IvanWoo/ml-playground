#!/bin/sh
set -euo pipefail

BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="${BASE_DIR}/../.."
VECTORS_DIR="${REPO_DIR}/notebooks/vectors"
TARGET_DIR="${VECTORS_DIR}/text_video_retrieval_engine/data"

(  
    mkdir -p $TARGET_DIR
    cd $TARGET_DIR
    # MSR-VTT-1kA test
    gdown --id 1cuFpHiK3jV9cZDKcuGienxTg1YQeDs-w
    unzip -q -o test.zip
    curl -L https://github.com/towhee-io/examples/releases/download/data/text_video_search.zip -O
    unzip -q -o text_video_search.zip
)
