# url = "https://secure.runescape.com/m=itemdb_oldschool/api/catalogue/items.json?category=1&alpha=c&page=1"
# response = urllib.request.urlopen(url)
# print(response.read())

__all__ = ["grandexchange", "restadapter"]


# garbage from testing, will be removed eventually.
if __name__ == "__main__":
    import grandexchange
    import restadapter

    ge = grandexchange.GrandExchange()
    print(ge, ge.get_category(1))

    # print(
    #     restadapter.call_api("https://secure.runescape.com/m=itemdb_rs/api/info.json")
    # )
