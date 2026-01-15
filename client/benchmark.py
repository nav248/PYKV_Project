import threading
import requests
import time

BASE_URL = "http://127.0.0.1:8000"
TOTAL_REQUESTS = 1000
THREADS = 10

def worker(start, end):
    for i in range(start, end):
        requests.post(
            f"{BASE_URL}/set",
            json={"key": f"key{i}", "value": f"value{i}"}
        )

def benchmark():
    threads = []
    start_time = time.time()

    per_thread = TOTAL_REQUESTS // THREADS

    for i in range(THREADS):
        t = threading.Thread(
            target=worker,
            args=(i * per_thread, (i + 1) * per_thread)
        )
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end_time = time.time()
    print(f"Total Requests: {TOTAL_REQUESTS}")
    print(f"Threads: {THREADS}")
    print(f"Time Taken: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    benchmark()
