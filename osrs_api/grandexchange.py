import restadapter


class GrandExchange:
    def __init__(self):
        self.base_url = "https://secure.runescape.com/m=itemdb_oldschool/api/"

    def get_category(self, category_id, starting_letter: str = None, page: int = None):
        url = self.base_url + "catalogue/category.json?category=" + str(category_id)

        if starting_letter:
            url += "&alpha=" + starting_letter

        if page:
            url += "&page=" + str(page)

        return restadapter.call_api(url)

    def get_item(self, item_id):
        url = self.base_url + "catalogue/detail.json?item=" + str(item_id)
        return restadapter.call_api(url)
