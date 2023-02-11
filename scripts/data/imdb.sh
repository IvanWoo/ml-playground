#!/bin/sh
set -euo pipefail

BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="${BASE_DIR}/../.."
DATA_DIR="${REPO_DIR}/notebooks/data"
IMDB_DIR="${DATA_DIR}/acl_imdb"

(
    mkdir -p $IMDB_DIR
    cd $IMDB_DIR
    curl -O https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz
    tar -xf aclImdb_v1.tar.gz
    rm -r aclImdb/train/unsup
)
