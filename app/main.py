class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    friends = [Person(person["name"], person["age"]) for person in people]
    for i in range(len(people)):
        spouse = list(people[i].items())[-1]
        if spouse[1] is not None:
            friend = Person.people[spouse[1]]
            setattr(friends[i], spouse[0], friend)
    return friends
