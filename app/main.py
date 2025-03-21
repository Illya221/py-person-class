class Person:
    people = {}  # Dictionary to store instances by name

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self  # Store instance by name


def create_person_list(people_list: list) -> None:
    # Step 1: Create all Person instances
    persons = []
    for person_dict in people_list:
        person = Person(person_dict["name"], person_dict["age"])
        persons.append(person)

    for person_dict in people_list:
        person = Person.people[person_dict["name"]]
        if "wife" in person_dict and person_dict["wife"] is not None:
            person.wife = Person.people[person_dict["wife"]]
        if "husband" in person_dict and person_dict["husband"] is not None:
            person.husband = Person.people[person_dict["husband"]]

    return persons
