import redis
from time import sleep

client = redis.Redis(host="localhost", port=6379, db=0)


while True:
    queue, payload = client.brpop(["queue-test"], timeout=0)
    job = payload.decode()
    print("job: ", job)
    sleep(0.5)


# on redis-cli:
# LPUSH jobs "task-hello"
# BRPOP jobs 0