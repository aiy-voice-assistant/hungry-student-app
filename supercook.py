import requests
from pprint import pprint


N_RECIPES = 2

def build_payload(ingredients):
    count = 0
    n_ingredients = len(ingredients)
    payload = "needsimage=0&kitchen="

    for i in ingredients:
        # if last item then do not add '%2C%20', ex: "egg%2C%20butter"
        if count == n_ingredients-1:
            if i is not None:
                payload += i
        else:
            if i is not None:
                payload += i + "%2C%20"

        count = count + 1

    payload += "&focus=&kw=&catname=%2C%2C&exclude=&start=0&undefined="

    return payload


def get_recipes(ingredients):
    url = "https://www.supercook.com/dyn/results"

    payload = build_payload(ingredients)

    headers = {
        'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0",
        'Accept': "application/json, text/plain, */*",
        'Accept-Language': "it-IT,it;q=0.8,en-US;q=0.5,en;q=0.3",
        'Accept-Encoding': "gzip, deflate, br",
        'Referer': "https://www.supercook.com/",
        'Content-Type': "application/x-www-form-urlencoded",
        'Content-Length': "67",
        'Connection': "keep-alive",
        'cache-control': "no-cache",
        'Postman-Token': "aeffaf87-d09f-444d-b87f-dab71b8b4db7"
        }

    response = requests.request("POST", url, data=payload, headers=headers).json()

    #pprint(response)

    count = 0
    recipes = {}
    needs = {}
    url = {}
    for r in response['results']:
        if r['displayurl'].find("allrecipes.com") != -1:
            recipes.update({count: r['title']})
            needs.update(({count: r['needs']}))
            url.update(({count: r['hash']}))
            # take only the first N_RECIPES recipes
            if count == N_RECIPES:
                break
    
            count = count + 1

    # pprint(recipes)

    return recipes, needs, url


def getRecipeName(ingredients):
    ingredients.sort()
    recipes, needs, urls = get_recipes(ingredients)
    
    return recipes, needs, urls