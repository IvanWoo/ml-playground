#!/bin/sh
set -euo pipefail

BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="${BASE_DIR}/../.."
DATA_DIR="${REPO_DIR}/notebooks/data"
CLIMATE_DIR="${DATA_DIR}/jena_climate"

(
    mkdir -p $CLIMATE_DIR
    cd $CLIMATE_DIR
    wget https://s3.amazonaws.com/keras-datasets/jena_climate_2009_2016.csv.zip
    unzip jena_climate_2009_2016.csv.zip
)
