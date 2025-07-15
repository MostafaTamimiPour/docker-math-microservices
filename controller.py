# controller.py
import requests
import time
from multiprocessing.dummy import Pool as ThreadPool

SERVICES = [
    ("adder",     "http://adder:5000/compute"),
    ("subtractor","http://subtractor:5001/compute"),
    ("multiplier","http://multiplier:5002/compute"),
    ("divider",   "http://divider:5003/compute"),
]

def fetch(service):
    name, url = service
    try:
        t0 = time.perf_counter()
        res = requests.get(url, timeout=5)
        elapsed = time.perf_counter() - t0
        data = res.json()
        return {
            "service": name,
            "result": data.get("result"),
            "time_s": elapsed
        }
    except Exception as e:
        return {
            "service": name,
            "error": str(e),
            "time_s": None
        }

def main():
    pool = ThreadPool(len(SERVICES))
    results = pool.map(fetch, SERVICES)
    pool.close()
    pool.join()

    print("\n=== Consolidated Results ===")
    for r in results:
        if "error" in r:
            print(f"{r['service']:10s} -> Error: {r['error']}")
        else:
            print(f"{r['service']:10s} -> {r['result']}   (time: {r['time_s']:.4f} s)")

if __name__ == "__main__":
    main()
