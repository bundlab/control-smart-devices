import requests

BASE_URL = "http://127.0.0.1:8000"


class APIService:

    @staticmethod
    def get_devices():
        response = requests.get(f"{BASE_URL}/devices")
        return response.json()