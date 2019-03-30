import requests


def get_restaurant():
    url = "https://it-partnerapi.just-eat.io/delivery/deliverablerestaurants?toLat=45.0663695&toLon=7.64986499999998"

    payload = ""
    headers = {
        'Authoriza'
        'accept': "application/json"
    }

    response = requests.request("GET", url, data=payload, headers=headers)

    print(response.text)
