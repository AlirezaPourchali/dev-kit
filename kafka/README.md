# kafka

Quick setup of a kafka cluster with controllers

```
helm repo add bitnami https://charts.bitnami.com/bitnami

helm upgrade my-kafka --install  bitnami/kafka --set global.imageRegistry="registry.docker.ir" --version 25.3.3
```

sample python [code](./app.py) for producer and consumer