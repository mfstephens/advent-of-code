import json
from pprint import pprint

def dayTwelve():
    json_data=open("day-12-input.json").read()

    data = json.loads(json_data)
    pprint(data)

dayTwelve()