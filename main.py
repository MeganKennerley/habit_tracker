import requests
from datetime import datetime
import os

USERNAME = os.environ.get("USERNAME")
TOKEN = os.environ.get("TOKEN")
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

add_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

headers = {
    "X-USER-TOKEN": TOKEN
}

today = datetime.now()

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours of code did you do today?: ")
}

response = requests.post(url=add_pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)