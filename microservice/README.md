# Deploy microservice with helmchart

Please edit [values](./values.yml) file , then install with:   

```bash
helm repo add app https://aahemm.github.io/helm-microservice

helm install microservice app/app --values values.yml --version 0.10.0
```

P.S: [Credit](https://github.com/aahemm/helm-microservice)