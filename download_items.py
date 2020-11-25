import requests
from tqdm import tqdm

from app.db.database import get_db
from app.items.models import Item

GAME_VERSION = "10.24.1"
LANGUAGE = "en_US"
ITEMS_URL = (
    f"http://ddragon.leagueoflegends.com/cdn/{GAME_VERSION}/data/{LANGUAGE}/item.json"
)
ITEMS_ASSETS_URL = "http://ddragon.leagueoflegends.com/cdn/10.24.1/img/item/"


def get_items():
    [db] = get_db()
    r = requests.get(ITEMS_URL)
    items_added = 0

    if r.status_code == 200:
        items_data = r.json()["data"]
        db.execute("truncate items CASCADE;")  # clears current items

        for id, item in tqdm(items_data.items()):
            if db.query(Item).get(id):
                continue

            image_url = ITEMS_ASSETS_URL + item["image"]["full"]

            new_item = Item(
                id=id,
                name=item["name"],
                description=item["description"],
                plaintext=item["plaintext"],
                image=image_url,
            )

            db.add(new_item)
            db.commit()
            items_added += 1

    print(f"Populating completed. Added {items_added} new item(s)")


if __name__ == "__main__":
    get_items()
