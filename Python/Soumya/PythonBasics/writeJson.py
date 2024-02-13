# write json data into a file ...

import json

dict1 = {"name": "Bob", "languages":["Enflish", "Afrikaans"]}
with open('person.txt', 'w') as jsonFile:
    json.dump(dict1, jsonFile)