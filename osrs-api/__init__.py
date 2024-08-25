import urllib.request

url = "https://secure.runescape.com/m=itemdb_oldschool/api/catalogue/items.json?category=1&alpha=c&page=1"
response = urllib.request.urlopen(url)
print(response.read())