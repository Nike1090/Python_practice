
persons = [
    {"first_name": "Max", "last_name": "Thompson", "age": 32},
    {"first_name": "Max", "last_name": "Hilton", "age": 35},
    {"first_name": "Rocky", "last_name": "Clans"},
    {"first_name": "Linda", "last_name": "Dimmer", "job": "Developer"},
]


def search_person(**attrs):
    person_list = []
    for key, value in attrs.items():
        person_list += \
            [
                person
                for person in persons
                if key in person and value == person[key]
            ]  # Slash is used for line continuation. 
               # It allows you to write a single logical line of code across multiple physical lines,
               #  making the code more readable and easier to maintain.
    return person_list


if __name__ == '__main__':
    print(search_person(first_name="Max"))
    print(search_person(last_name="Clans"))
    print(search_person(last_name="Dimmer"))
    print(search_person(last_name="No One"))


