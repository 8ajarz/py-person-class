class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    friends = [Person(person["name"], person["age"]) for person in people]
    for friend in friends:
        spouse = [
            list(person.items())[-1]
            for person in people
            if person["name"] == friend.name
        ][0]
        if spouse[1] is not None:
            setattr(friend, spouse[0], Person.people[spouse[1]])
    return friends
