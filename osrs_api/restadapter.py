import urllib.request


def call_api(url):
    """Calls the API with the given URL and returns the response."""
    response = urllib.request.urlopen(url)
    return response.read().decode("utf-8")
