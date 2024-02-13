import json

with open('sample.json', 'r') as f:
    data = json.load(f)
print(data)

# converting dictionary to json ...
dict1 = {"name": "John", "age": 12}
print(type(dict1))
dict1_json = json.dumps(dict1)
print(dict1_json)
print(type(dict1_json))

jsonString =  '[[{"a":1, "b":2}], [{"c":3, "d": 4}]]'
dict = json.loads(jsonString)

# converting json to dictionary ...
print((dict[0][0]))
