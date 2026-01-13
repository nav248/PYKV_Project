import time
from server.recovery import recover

def start_replica(store, interval=5):
    while True:
        recover(store)
        time.sleep(interval)
