import requests

BASE_URL = "http://127.0.0.1:8000"

def set_key(key, value):
    r = requests.post(f"{BASE_URL}/set", json={"key": key, "value": value})
    print(r.json())

def get_key(key):
    r = requests.get(f"{BASE_URL}/get/{key}")
    print(r.json())

def delete_key(key):
    r = requests.delete(f"{BASE_URL}/delete/{key}")
    print(r.json())

if __name__ == "__main__":
    set_key("city", "Hyderabad")
    set_key("college", "CBIT")
    set_key("course", "AI & Data Science")

    get_key("city")
    get_key("college")
    get_key("course")

    delete_key("college")
    get_key("college")
