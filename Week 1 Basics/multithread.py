import requests
from concurrent.futures import ThreadPoolExecutor
import time 

url="http://192.168.1.2:30001"
TOTAL_REQUESTS=5000
WORKERS=20

def hit(i):
    try:
        r=requests.get(url,timeout=3)
        return r.status_code
    except Exception as e:
        return (e)

start=time.time()

with ThreadPoolExecutor(max_workers=WORKERS) as executor:
    results=list(executor.map(hit,range(TOTAL_REQUESTS)))

end=time.time()

success=results.count(200)

print(f"Sucess {success}/{TOTAL_REQUESTS}")
print(f"Time: {end-start:.2f}s")