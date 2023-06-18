#!/bin/sh
set -euo pipefail

BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="${BASE_DIR}/../.."
VECTORS_DIR="${REPO_DIR}/notebooks/vectors"
TARGET_DIR="${VECTORS_DIR}/audio_fingerprint/data"

(  
    mkdir -p $TARGET_DIR
    cd $TARGET_DIR
    # subset of GTZAN
    curl -L https://github.com/towhee-io/examples/releases/download/data/audio_fp.zip -O
    unzip -q -o audio_fp.zip
)
