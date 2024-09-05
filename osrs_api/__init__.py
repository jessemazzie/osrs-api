import json
import logging

__all__ = ["grandexchange", "restadapter"]


# garbage from testing, will be removed eventually.
if __name__ == "__main__":
    import grandexchange
    import restadapter

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s %(levelname)s %(message)s",
        handlers=[logging.StreamHandler()],
    )
    ge = grandexchange.GrandExchange()
    items = json.loads(ge.get_items("c", 1))["items"]
    print(len(items))
    for item in items:
        print(f"Name: {item['name']}")
        print(f"ID: {item['id']}")
        print(f"Price_current: {item['current']}")
        print(f"Price_today: {item['today']}")
        print("\n")
    # print(
    #     restadapter.call_api("https://secure.runescape.com/m=itemdb_rs/api/info.json")
    # )
