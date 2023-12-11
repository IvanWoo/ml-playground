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
pdm run verify/tf.py
```

```sh
Metal device set to: Apple M1 Max

systemMemory: 64.00 GB
maxCacheSize: 24.00 GB

2023-12-10 22:29:19.500955: I tensorflow/core/common_runtime/pluggable_device/pluggable_device_factory.cc:305] Could not identify NUMA node of platform GPU ID 0, defaulting to 0. Your kernel may not have been built with NUMA support.
2023-12-10 22:29:19.501092: I tensorflow/core/common_runtime/pluggable_device/pluggable_device_factory.cc:271] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 0 MB memory) -> physical PluggableDevice (device: 0, name: METAL, pci bus id: <undefined>)
2023-12-10 22:29:20.641573: W tensorflow/core/platform/profile_utils/cpu_utils.cc:128] Failed to get CPU frequency: 0 Hz
Epoch 1/5
/opt/homebrew/Caskroom/miniconda/base/envs/ml-playground/lib/python3.9/site-packages/tensorflow/python/util/dispatch.py:1082: UserWarning: "`sparse_categorical_crossentropy` received `from_logits=True`, but the `output` argument was produced by a sigmoid or softmax activation and thus does not represent logits. Was this intended?"
  return dispatch_target(*args, **kwargs)
2023-12-10 22:29:21.922694: I tensorflow/core/grappler/optimizers/custom_graph_optimizer_registry.cc:113] Plugin optimizer for device_type GPU is enabled.
782/782 [==============================] - 50s 60ms/step - loss: 4.7830 - accuracy: 0.0682
Epoch 2/5
782/782 [==============================] - 48s 62ms/step - loss: 4.2318 - accuracy: 0.1223
Epoch 3/5
782/782 [==============================] - 48s 62ms/step - loss: 4.1582 - accuracy: 0.1165
Epoch 4/5
782/782 [==============================] - 48s 61ms/step - loss: 3.9094 - accuracy: 0.1440
Epoch 5/5
782/782 [==============================] - 48s 62ms/step - loss: 3.6939 - accuracy: 0.1772
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
