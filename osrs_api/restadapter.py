import urllib.request


def call_api(url):
    response = urllib.request.urlopen(url)
    return response.read().decode("utf-8")
