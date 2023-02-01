# ml-playground

## prerequisites

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

## ref

- [Get started with tensorflow-metal](https://developer.apple.com/metal/tensorflow-plugin/)
- [PyTorch 1.13: beta versions of functorch and improved support for Apple’s new M1 chips are now available](https://github.com/pytorch/pytorch/releases/tag/v1.13.0)
- [Installing PyTorch on Apple M1 chip with GPU Acceleration](https://towardsdatascience.com/installing-pytorch-on-apple-m1-chip-with-gpu-acceleration-3351dc44d67c)
- [fchollet/deep-learning-with-python-notebooks](https://github.com/fchollet/deep-learning-with-python-notebooks)
