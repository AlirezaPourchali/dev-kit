# Mysql - master/slave depoyment

A quick setup for mysql master/slave deployment with a bitnami chart for only experiment purposes and it is not advised to use bitnami when you dont know how it works and evolves.     

```
helm repo add bitnami https://charts.bitnami.com/bitnami    

helm install my-mysql bitnami/mysql --set image.registry="docker.iranrepo.ir" --set architecture="replication" --set secondary.replicaCount=2 --version 9.12.5

```

It will deploy 1 primary instance of mysql and two secondary instances which replicate from the master instance.    
2 service , which is kind of a loadbalancer ( one for primary one for secondary ) , and 2 headless services for them to discover pods.    

Here is a sample python [code](./app.py) for connecting and executing commands in MysqlDB