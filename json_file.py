# JSON is commonly used with APIs . we will learn how to parse JSOn into a python Dictionary

import json

# Sample JSON
detailJSON = '{"first_name": "Augustine", "last_name": "Emeka", "age": 35}'

# Parse to Dictionary
detail = json.loads(detailJSON)

print(detail)
print(detail['first_name'])

# geting back to JSON from a diction

carDict = {'make': 'Toyota', 'model': 'Camry', 'year': 2014}

carJSON = json.dumps(carDict)
print(carJSON)