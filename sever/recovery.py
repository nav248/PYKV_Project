from server.persistence import LOG_FILE

def recover(store):
    try:
        with open(LOG_FILE, "r") as f:
            for line in f:
                parts = line.strip().split(" ", 2)
                if parts[0] == "SET":
                    store.cache.put(parts[1], parts[2])
                elif parts[0] == "DEL":
                    store.cache.delete(parts[1])
    except FileNotFoundError:
        pass
