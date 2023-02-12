#!/bin/sh
set -euo pipefail

BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="${BASE_DIR}/../.."
DATA_DIR="${REPO_DIR}/notebooks/data"
GLOVE_DIR="${DATA_DIR}/glove"

(
    mkdir -p $GLOVE_DIR
    cd $GLOVE_DIR
    wget http://nlp.stanford.edu/data/glove.6B.zip
    unzip -q glove.6B.zip
)
