PyKV – In-Memory Key-Value Store with Persistence
Overview:

PyKV is a lightweight in-memory key-value store built using Python and FastAPI.
It improves upon a normal Python dictionary by adding LRU caching, disk persistence, crash recovery, and concurrent client handling.
The project is inspired by real-world systems like Redis.

Problem Statement

Python dictionaries are fast but lack:

Eviction policy

Persistence

Concurrency support

Crash recovery

Goal:
To build a scalable key-value store with LRU caching, disk persistence, recovery, and concurrency support.

 Features

Fast in-memory storage

LRU (Least Recently Used) cache eviction

Append-only disk persistence

Automatic crash recovery

REST APIs using FastAPI

Concurrent client handling

Performance benchmarking

Tech Stack

1.Python

2.FastAPI

3.LRU Cache (OrderedDict)

4.Append-only log file

5.Multithreading

📂 Project Structure
server/        → Backend logic
client.py     → API client
benchmark.py  → Performance testing
requirements.txt

⚙️ How to Run
Install dependencies
pip install -r requirements.txt

Start server
uvicorn server.main:app --reload

Run client
python client.py

Run benchmark
python benchmark.py

API Endpoints

POST /set – Store key-value pair

GET /get/{key} – Retrieve value

DELETE /delete/{key} – Delete key

Persistence & Recovery

All operations are logged to a file

On restart, data is recovered by replaying the log

Ensures no data loss after crash

⚠️ Limitations

Single-node system

No authentication

No TTL support



Conclusion:

PyKV demonstrates core backend concepts such as caching, persistence, recovery, and concurrency, making it a strong foundation for understanding real-world key-value storage systems.
