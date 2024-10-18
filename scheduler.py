import requests
import os
import time
from dotenv import load_dotenv

load_dotenv()

schedule_time = int(os.getenv('SCHEDULE_TIME'))
url = os.getenv('API_URL')
x_api_token = os.getenv('X_API_TOKEN')


def hit_api():
    print(url)
    try:
        headers = {
            "x-api-token": x_api_token
        }
        response = requests.post(url, headers=headers)
        if response.status_code == 200:
            print("API response received successfully.")
            print(response.content,response.status_code)
        else:
            print(f"Failed to hit API. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error hitting API: {e}")

def run_scheduler():
    while True:
        hit_api()
        print(f"Waiting for {schedule_time}s to hit the API again...")
        time.sleep(schedule_time)

if __name__ == "__main__":
    run_scheduler()
