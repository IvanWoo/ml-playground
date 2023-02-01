#!/bin/sh
set -euo pipefail

BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="${BASE_DIR}/../.."
DATA_DIR="${REPO_DIR}/notebooks/data"
PETS_DIR="${DATA_DIR}/oxford-iiit-pet"

(
    cd tools
    yarn install
    # https://academictorrents.com/details/b18bbd9ba03d50b0f7f479acc9f4228a408cecc1
    yarn run webtorrent download "magnet:?xt=urn:btih:b18bbd9ba03d50b0f7f479acc9f4228a408cecc1&tr=https%3A%2F%2Facademictorrents.com%2Fannounce.php&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce" --out $DATA_DIR
)
(
    cd $PETS_DIR
    # wget http://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz
    # wget http://www.robots.ox.ac.uk/~vgg/data/pets/data/annotations.tar.gz
    tar -xf images.tar.gz
    tar -xf annotations.tar.gz
)
