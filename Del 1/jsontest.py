import json

x = {
    'name': 'Bob',
    'age': '25',
    'city': 'Los Angeles'
}
with open('output.json', 'w') as f:
    json.dump(x, f)