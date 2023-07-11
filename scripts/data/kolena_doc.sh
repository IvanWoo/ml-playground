#!/bin/sh
set -euo pipefail

BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="${BASE_DIR}/../.."
DATA_DIR="${REPO_DIR}/langchain/data"

(
    rm -rf $DATA_DIR
    mkdir -p $DATA_DIR
    cd $DATA_DIR
    git clone --depth 1 https://github.com/kolenaIO/kolena.git
)
