# Redis-Cluster

This helm-chart uses bitnami/redis-cluter to deploy redis in kubernetes.

Install:
```
helm upgrade --install redis bitnami/redis-cluster \
--set image.registry=docker.iranrepo.ir \
--version 9.0.11
```

## Note
You should update the password of the database. You can get it with the below command:
```
helm status redis
```