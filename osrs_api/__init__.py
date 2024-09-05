import json

__all__ = ["grandexchange", "restadapter"]


# garbage from testing, will be removed eventually.
if __name__ == "__main__":
    import grandexchange
    import restadapter

    ge = grandexchange.GrandExchange()
    items = json.loads(ge.get_items("c", 1))["items"]
    print(items.keys())
    # print(
    #     restadapter.call_api("https://secure.runescape.com/m=itemdb_rs/api/info.json")
    # )
