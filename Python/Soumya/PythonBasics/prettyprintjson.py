import json
person = '{"name": "Bob", "languages": "English"}'
personDict = json.loads(person)
print(type(personDict))
print(json.dumps(personDict, indent = 4, sort_keys=True))