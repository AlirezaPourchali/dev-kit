# MariaDB - galera depoyment

MariaDB Galera Cluster is a virtually synchronous multi-primary cluster for MariaDB.

Its an Active-Active setup and every replica can accept read/write connections     
You can also join new nodes to the cluster as well.    

This is a quick setup for a galera deployment with bitnami chart for only experiment purposes and it is not advised to use bitnami when you dont know how it works and evolves.  

```
helm repo add bitnami https://charts.bitnami.com/bitnami    

helm install my-mariadb-galera bitnami/mariadb-galera \
--set image.registry="docker.iranrepo.ir" \
--set replicaCount=3 \ 
--version 10.0.1

```

It will deploy 3 replicas of mariadb and two services , one headless and the other to loadbalance connections between replicas

Here is a sample python [code](./app.py) for connecting and executing commands in MariaDB