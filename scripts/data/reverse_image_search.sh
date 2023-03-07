#!/bin/sh
set -euo pipefail

BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="${BASE_DIR}/../.."
VECTORS_DIR="${REPO_DIR}/notebooks/vectors"
TARGET_DIR="${VECTORS_DIR}/text_image_search_engine/data"

(  
    mkdir -p $TARGET_DIR
    cd $TARGET_DIR
    curl -L https://github.com/towhee-io/examples/releases/download/data/reverse_image_search.zip -O
    unzip -q -o reverse_image_search.zip
)
