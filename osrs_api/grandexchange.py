import restadapter


class GrandExchange:
    def __init__(self):
        self.base_url = 'https://secure.runescape.com/m=itemdb_oldschool/api/catalogue/detail.json?item='

    def get_item(self, item_id):
        url = self.base_url + str(item_id)
        return restadapter.call_api(url)