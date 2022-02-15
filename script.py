import json

import yaml
import sys

args = sys.argv

if len(args) <= 1:
    print('ERROR: Need to pass yaml file location!')
    exit()

file_location = args[1]

arr = {}


def nested_key(key, items):
    if type(items) is dict:
        for nested_key_key in items:
            nested_key('%s.%s' % (key, nested_key_key), items[nested_key_key])
    else:
        arr[key] = items


with open(file_location) as file:
    items = yaml.load(file, Loader=yaml.FullLoader)

    for key in items:
        nested_key(key, items[key])

    print(json.dumps(arr, indent=4, sort_keys=True))
