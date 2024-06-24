"""
JSON Writer
"""
import json

if __name__ == '__main__':
    with open('data.json', "w") as file:
        data = {
            "Person 1": {
                "first_name": "Max",
                "last_name": "colidge",
                "year": 2024,
                "money": 230.5
            }
        }

        json.dump(data, file, indent=4)

    with open("data.json", "r") as file:
        data = json.load(file)
        print(data["Person 1"]["first_name"])

    with open("data.json", "r") as file:
        data = json.load(file)
        data.update({
             "Person 2": {
                "first_name": "Derex",
                "last_name": "colidge",
                "year": 2024,
                "money": 230.5
             }
        })
    
    # commit updated data
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

    
    with open("data.json", "r") as file:
        data = json.load(file)
        print(data["Person 2"]["first_name"])