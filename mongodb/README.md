# mongodb-sharded

Install mongodb-sharded on k8s with the help of bitnami chart:   

```bash
helm upgrade mongoshard --install bitnami/mongodb-sharded \
--set shards=3,global.imageRegistry="docker.iranrepo.ir" \
--set configsvr.replicaCount="3" \
--set shardsvr.dataNode.replicaCount="2",mongos.replicaCount=2
```

mongodb sharded structure is made of mainly 3 parts:

* mongos : coordinator or a router for the incoming connections from the clients
* configserver: it stores data about the current mongodb cluster and gives mongos info for coordination
* shards : where the actuall data is stored , shards are replicated to each instance (you should read more about it)

This helm chart will deploy:

* 3 shards 
* and the shard instances are replicated (2*3 instances for shards)
* 3 config server instances
* 2 mongos instances

this is just a quick setup and it is not advised for production because there will be more than enough complexity

python [code](app.py) example for connection to mongodb
