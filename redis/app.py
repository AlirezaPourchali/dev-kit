from redis.cluster import RedisCluster as Redis
import json

client = Redis(host='redis-redis-cluster', port=6379, password="BMbgOzoWrw")

# insert data
client.set("name", "saleh")

# get data
client.get("name")

# insert json
data = {"name": "Alice", "age": 30, "email": "alice@example.com"}

client.set("user_data", json.dumps(data))