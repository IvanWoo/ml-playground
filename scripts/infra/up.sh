#!/bin/sh
# This file is autogenerated - DO NOT EDIT!
set -euo pipefail
BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="${BASE_DIR}/../.."
(
cd ${REPO_DIR}
kubectl create namespace milvus --dry-run=client -o yaml | kubectl apply -f -
helm repo add milvus https://milvus-io.github.io/milvus-helm/
helm upgrade --install my-milvus milvus/milvus --namespace milvus -f helm/milvus/values.yaml
)