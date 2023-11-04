# ml-playground

## prerequisites

### git

```sh
brew install git git-lfs
git lfs install
```

### conda

```sh
brew install --cask miniconda
conda init fish
```

```sh
conda create -n ml-playground python=3.9 -y
conda activate ml-playground
```

### tensorflow

```sh
conda install -c apple tensorflow-deps
```

verify the GPU acceleration

```sh
python verify/tf.py
```

![tf gpu verification](assets/verify_tf_gpu.png)

### pytorch

verify the GPU acceleration

```sh
python verify/pytorch.py
```

### [pdm](https://pdm.fming.dev/latest/)

```sh
pdm install
```

### node

some downloading tools depends on the node ecosystem

```sh
brew install fnm
```

## notebooks

activate the env

```sh
conda activate ml-playground
```

open the jupyter lab

```sh
jupyter lab
```

## optional components

### pipx

```sh
pipx install gdown
```

### infra

tl;dr: `./scripts/infra/up.sh`

tl;dr: `./scripts/infra/down.sh`

#### milvus

start

```sh
kubectl create namespace milvus --dry-run=client -o yaml | kubectl apply -f -
helm repo add milvus https://milvus-io.github.io/milvus-helm/
helm upgrade --install my-milvus milvus/milvus --namespace milvus -f helm/milvus/values.yaml
```

connect

```sh
kubectl port-forward svc/my-milvus --namespace milvus 19530
```

view the data in [Attu](http://127.0.0.1:3000/?#/collections)

```sh
kubectl port-forward svc/my-milvus-attu --namespace milvus 3000
```

clean

```sh
helm uninstall --namespace milvus my-milvus
kubectl delete namespace milvus
```

#### pgvector

build the image

```sh
nerdctl --namespace k8s.io build -t my/postgresql-pgvector -f helm/postgresql/Dockerfile helm/postgresql/
```

start

```sh
kubectl create namespace pgvector --dry-run=client -o yaml | kubectl apply -f -
helm upgrade --install my-pgvector oci://registry-1.docker.io/bitnamicharts/postgresql --namespace pgvector -f helm/postgresql/values.yaml
```

enable pgvector extension

```sh
kubectl run my-pgvector-postgresql-client --rm --tty -i --restart='Never' --namespace pgvector --image my/postgresql-pgvector:latest --image-pull-policy='Never' --env="PGPASSWORD=demo_password" --command -- psql --host my-pgvector-postgresql -U postgres -d postgres -p 5432
```

```sql
CREATE EXTENSION vector;
```

```sql
postgres=# \dx
                        List of installed extensions
  Name   | Version |   Schema   |                Description
---------+---------+------------+--------------------------------------------
 plpgsql | 1.0     | pg_catalog | PL/pgSQL procedural language
 vector  | 0.4.4   | public     | vector data type and ivfflat access method
(2 rows)
```

```sh
kubectl port-forward svc/my-pgvector-postgresql --namespace pgvector 5432
```

clean

```sh
helm uninstall --namespace pgvector my-pgvector
kubectl delete namespace pgvector
```

## ref

- [Get started with tensorflow-metal](https://developer.apple.com/metal/tensorflow-plugin/)
- [PyTorch 1.13: beta versions of functorch and improved support for Apple’s new M1 chips are now available](https://github.com/pytorch/pytorch/releases/tag/v1.13.0)
- [Installing PyTorch on Apple M1 chip with GPU Acceleration](https://towardsdatascience.com/installing-pytorch-on-apple-m1-chip-with-gpu-acceleration-3351dc44d67c)
- [fchollet/deep-learning-with-python-notebooks](https://github.com/fchollet/deep-learning-with-python-notebooks)
