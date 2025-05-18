class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    marriage = ("wife", "husband")
    friends = [Person(person["name"], person["age"]) for person in people]
    for friend in friends:
        person = [dct for dct in people if dct["name"] == friend.name][0]
        spouse = marriage["husband" in person]
        partner = spouse, person[spouse]
        if partner[1] is not None:
            setattr(friend, partner[0], Person.people[partner[1]])
    return friends
