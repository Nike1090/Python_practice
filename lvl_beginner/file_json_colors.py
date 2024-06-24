import json

FILE = "C:\\Users\\nike9\\OneDrive\\Python practice\\colors.json"

# with open(FILE, 'r') as json_file:
#     # Load the JSON data into a dictionary
#     colorsDict = json.load(json_file)
json_file = open(FILE, "r")
colorsDict = json.load(json_file)

for color in colorsDict["colors"]:
    print(f'Color: {color["color"]} | Code: {color["value"]}')

json_file.close()