LOG_FILE = "data/kv.log"

def log_set(key, value):
    with open(LOG_FILE, "a") as f:
        f.write(f"SET {key} {value}\n")

def log_delete(key):
    with open(LOG_FILE, "a") as f:
        f.write(f"DEL {key}\n")
