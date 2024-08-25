from osrs_api.restadapter import call_api
import json


def test_call_api_info():
    """Test the call_api function with the info endpoint."""
    url = "https://secure.runescape.com/m=itemdb_rs/api/info.json"
    response = call_api(url)
    json_response = json.loads(response)
    print(json_response)

    assert response is not None
    assert "lastConfigUpdateRuneday" in json_response
