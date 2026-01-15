from fastapi import FastAPI, HTTPException

from server.models import SetRequest
from server.recovery import recover
from server.store import KeyValueStore



app = FastAPI(title="PyKV Store")
store = KeyValueStore(capacity=2)

# Recover data on startup
recover(store)

@app.get("/get/{key}")
async def get_value(key: str):
    value = await store.get(key)
    if value is None:
        raise HTTPException(status_code=404, detail="Key not found")
    return {"key": key, "value": value}

@app.post("/set")
async def set_value(data: SetRequest):
    await store.set(data.key, data.value)
    return {"status": "OK"}

@app.delete("/delete/{key}")
async def delete_value(key: str):
    await store.delete(key)
    return {"status": "Deleted"}
import threading
from server.replication import start_replica

replica_thread = threading.Thread(
    target=start_replica,
    args=(store,),
    daemon=True
)
replica_thread.start()
