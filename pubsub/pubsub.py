from redis import StrictRedis
from time import strftime, sleep

client = StrictRedis(host='localhost', port=6379, db=0)
sub = client.pubsub()
sub.subscribe('channel-test')

while True:
    m = sub.get_message()
    now = strftime("%Y-%m-%d %H:%M:%S")
    if m: print(f"{now} {m['data']}")
    else: print(f"{now} no message")
    sleep(0.5)


# install redis
# on terminal: 
# redis-cli
# publish channel-test "hello"
