import json
import operator
from pprint import pprint


def order_food(name):
    deliveroo = {}
    glovo = {}
    justeat = {}
    result = {}

    with open('foods/deliveroo.json') as json_data:
        deliveroo = json.load(json_data)
        # pprint(deliveroo)

    with open('foods/glovo.json') as json_data:
        glovo = json.load(json_data)
        # pprint(fedora)

    with open('foods/justeat.json') as json_data:
        justeat = json.load(json_data)
        # pprint(justeat)

    if name in deliveroo:
        result.update(({"deliveroo": deliveroo[name]}))
    else:
        result.update(({"deliveroo": -1}))

    if name in glovo:
        result.update(({"glovo": glovo[name]}))
    else:
        result.update(({"glovo": -1}))

    if name in deliveroo:
        result.update(({"just eat": deliveroo[name]}))
    else:
        result.update(({"just eat": -1}))

    result = sorted(result.items(), key=operator.itemgetter(1), reverse=True)
    key, value = result.pop()

    return key, value

