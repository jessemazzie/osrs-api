import logging
from restadapter import call_api


class GrandExchange:
    def __init__(self):
        self.base_url = "https://secure.runescape.com/m=itemdb_oldschool/api/"

    # /CATALOGUE/ endpoints
    def get_category(
        self, starting_letter: str = None, page: int = None, category_id: int = 1
    ):
        """/api/catalogue/items.json?category=1&alpha={starting_letter}&page={page}
        Gets a specific category of items from the grand exchange. Optionally accepts a starting letter (of item name) and page number.
        """
        url = self.base_url + "catalogue/category.json?category=" + str(category_id)
        logging.info(f"Category ID: {category_id}")
        logging.info(f"Current URL: {url}")

        if starting_letter:
            url += "&alpha=" + starting_letter
            logging.info(f"Starting letter: {starting_letter}")
            logging.info(f"Current URL: {url}")

        if page:
            url += "&page=" + str(page)
            logging.info(f"Page: {page}")
            logging.info(f"Current URL: {url}")

        logging.info(f"Final URL: {url}")
        return call_api(url)

    def get_item(self, item_id):
        """/api/catalogue/detail.json?item={item_id}
        Gets a single item by its item id."""
        url = self.base_url + "catalogue/detail.json?item=" + str(item_id)
        logging.info(f"Item ID: {item_id}")

        logging.info(f"Final URL: {url}")
        return call_api(url)

    def get_items(self, starting_letter: str, page: int, category_id: int = 1):
        """/api/catalogue/items.json?category=1&alpha={starting_letter}&page={page}
        Gets a list of items from the grand exchange. Optionally accepts a starting letter (of item name) and page number.
        """
        url = self.base_url + "catalogue/items.json?category=" + str(category_id)
        logging.info(f"Category ID: {category_id}")
        logging.info(f"Current URL: {url}")

        if starting_letter:
            url += "&alpha=" + starting_letter
            logging.info(f"Starting letter: {starting_letter}")
            logging.info(f"Current URL: {url}")

        if page:
            url += "&page=" + str(page)
            logging.info(f"Page: {page}")
            logging.info(f"Current URL: {url}")

        logging.info(f"Final URL: {url}")
        return call_api(url)
