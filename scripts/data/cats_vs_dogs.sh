#!/bin/sh
set -euo pipefail

kaggle competitions download -c dogs-vs-cats -p ./notebooks/data/cats_vs_dogs
(
    cd notebooks/data/cats_vs_dogs
    unzip -qq dogs-vs-cats.zip
    unzip -qq train.zip
)
