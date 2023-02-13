#!/bin/sh
set -euo pipefail

BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="${BASE_DIR}/../.."
DATA_DIR="${REPO_DIR}/notebooks/data"
TARGET_DIR="${DATA_DIR}/spa_eng"

(
    mkdir -p $TARGET_DIR
    cd $TARGET_DIR
    wget http://storage.googleapis.com/download.tensorflow.org/data/spa-eng.zip
    unzip -q spa-eng.zip
)
