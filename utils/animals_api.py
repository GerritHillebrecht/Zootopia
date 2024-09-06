import requests
from config import API_KEY, API_BASE_URL

headers = {
    "X-Api-Key": API_KEY
}


def fetch_animals(animal: str) -> list:
    response = requests.get(
        f"{API_BASE_URL}?name={animal}",
        headers=headers
    )

    if response.status_code == requests.codes.ok:
        return response.json()

    return []
