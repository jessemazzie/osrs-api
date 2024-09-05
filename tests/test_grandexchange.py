from osrs_api import grandexchange
import json

test_cases = [
    {"name": "Saradomin godsword", "item_id": 11806},
    {"name": "Rune scimitar", "item_id": 1333},
    {"name": "Green partyhat", "item_id": 1044},
]


def test_get_item():
    ge = grandexchange.GrandExchange()
    for test_case in test_cases:
        item_name = test_case["name"]
        item_id = test_case["item_id"]

        item = json.loads(ge.get_item(item_id))["item"]
        print(item)
        assert item["name"] == item_name


def test_get_items():
    ge = grandexchange.GrandExchange()
    items = json.loads(ge.get_items("s", 1))["items"]
    print(items)
