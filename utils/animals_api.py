import requests
import os


def get_headers():
    return {
        "X-Api-Key": os.getenv('API_KEY')
    }


def fetch_animals(animal: str) -> list:
    response = requests.get(
        f"{os.getenv("API_BASE_URL")}?name={animal}",
        headers=get_headers()
    )

    if response.status_code == requests.codes.ok:
        return response.json()

    return []
