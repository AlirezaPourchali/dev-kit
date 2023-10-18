# postgres HA 

Here is a fast deployment of a postgres ha architechture with bitnami chart.    

it deploys:   

* Masters and slaves instances 

* In those master and slaves there is repmgr (replication manager) which does the failover when the master instance is down

* It also deploys pgpool which proxies queries . write queries goes through to the master and read queries to the slaves 

* 3 different services , one for pgpool , one for pg instances and one headless service for discovering ip's    

This deployment is only experiment purposes and not advised in production.    

Install the chart: 
```bash
helm install my-postgresql bitnami/postgresql-ha \
--set global.imageRegistry="docker.iranrepo.ir" \
--set postgresql.replicaCount=3 \ 
--version 12.0.4
```

Use `POSTGRES_PASSWORD` in your python code and pgpool service name in hostname

Here is a sample python [code](./app.py)