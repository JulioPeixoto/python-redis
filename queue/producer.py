import redis

client = redis.Redis(host="localhost", port=6379, db=0)

client.lpush("queue-test", "message1")
client.lpush("queue-test", "message2")
client.lpush("queue-test", "message3")
