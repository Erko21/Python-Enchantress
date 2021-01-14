import requests


def make_request(address):
    requests.get(address)
    return True


def parse_response(last, month):
    response = make_request("http://company.com/{last}/{month}")
    if response:
        return "Successful request"
    else:
        return "Error in request"