from requests import request
from json import loads


def get_currencies():
    req_response = request("GET", "http://api.coincap.io/v2/assets/", headers={}, data={})
    json_data = loads(req_response.text.encode('utf8'))
    dict_data = {i['symbol']: i['id'] for i in json_data['data']}
    return dict_data


currencies = get_currencies()
