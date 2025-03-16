import json
json_file = 'data.json'
json_data = {}

with open(json_file, 'r') as file:
    json_data = json.load(file)
json_data["price"]=900
with open(json_file, 'w') as file:
    file.write(str(json_data))
