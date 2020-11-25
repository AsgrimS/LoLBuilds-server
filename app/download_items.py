import requests

ITEMS_URL = "http://ddragon.leagueoflegends.com/cdn/10.23.1/data/en_US/item.json"


def get_items():
    r = requests.get(ITEMS_URL)
    if r.status_code == 200:
        items_data = r.json()["data"]
        response = []
        for id, item in items_data.items():
            response.append({"id": id, "item": item})
        return response
