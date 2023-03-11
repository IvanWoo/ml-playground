# bentoml

## quickstart

train and save the model

```sh
pdm run python train_model.py
pdm run python save_model_to_bento.py
```

verify the model exists on bentoml

```sh
$ pdm run bentoml models list

 Tag                        Module           Size      Creation Time
 iris_clf:suw5eyv7swes2hr2  bentoml.sklearn  6.03 KiB  2023-03-10 17:47:49
```

serve the model locally

```sh
pdm run bentoml serve service:svc --reload
```

call the service

```sh
$ curl -X POST \
   -H "content-type: application/json" \
   --data "[[5.9, 3, 5.1, 1.8]]" \
   http://127.0.0.1:3000/classify

[2]
```

build the bento

```sh
pdm run bentoml build
```

serve the model from the just build bento

```sh
pdm run bentoml serve iris_classifier:latest --production
```

generate the docker image

FIXME: nerdctl doesn't work due to no `BUILDKIT_HOST`

```sh
Both buildkitd and BUILDKIT_HOST are not found. Ensure to use either of them.
To run a portable buildkitd (via container), do the following in a terminal:
    /Applications/Rancher Desktop.app/Contents/Resources/resources/darwin/bin/docker run -d --name buildkitd --privileged moby/buildkit:master
    export BUILDKIT_HOST=docker-container://buildkitd
```

```sh
pdm run bentoml containerize --opt platform=linux/amd64 --backend nerdctl iris_classifier:latest
```
