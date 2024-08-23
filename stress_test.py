import requests
import time
from concurrent.futures import ThreadPoolExecutor

url = "http://172.22.2.150:8001/api/indicator/pocket_index1?code=0050"
num_requests = 200  # 要發送的總請求數
concurrent_requests = 30  # 並發請求數量


def send_request(_):
    try:
        response = requests.get(url)
        return response.status_code
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

def stress_test():
    start_time = time.time()

    with ThreadPoolExecutor(max_workers=concurrent_requests) as executor:
        results = list(executor.map(send_request, range(num_requests)))

    end_time = time.time()

    success_count = sum(1 for result in results if result == 200)
    failure_count = num_requests - success_count

    print(f"Total requests: {num_requests}")
    print(f"Successful requests: {success_count}")
    print(f"Failed requests: {failure_count}")
    print(f"Time taken: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    stress_test()