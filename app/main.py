class Person:
    people = dict()

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    persons = list()

    for person in people:
        persons.append(Person(person["name"], person["age"]))

    for person in people:
        if person.get("wife"):
            Person.people[person["name"]].wife = Person.people.get(person.get("wife"))
        elif person.get("husband"):
            Person.people[person["name"]].husband = Person.people.get(person.get("husband"))
        else:
            pass
    return persons
