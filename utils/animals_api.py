import requests
import os


def get_headers():
    """
    Creates the header for the API Requests.
    :return: DICT with API-key header
    """
    return {
        "X-Api-Key": os.getenv('API_KEY')
    }


def fetch_animals(search_str: str) -> list:
    """
    Fetches animals from api and returns the json parsed list.
    :param search_str: animal to search for as str.
    :return: list of animals. Empty if nothing is found.
    """
    response = requests.get(
        f"{os.getenv("API_BASE_URL")}?name={search_str}",
        headers=get_headers()
    )

    if response.status_code == requests.codes.ok:
        return response.json()

    return []
