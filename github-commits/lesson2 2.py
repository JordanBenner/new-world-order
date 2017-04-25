class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def greet(self):
        print(self.make, self.model, self.year)


class Person:
    def __init__(self, name, email, phone, friends=[]):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = friends

    def add_friend(self, friend):
        self.friends.append(friend)

    def print_contact_info(self):
        print(self.name + "'s contact_info: " + self.email, self.phone)


sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@hotmail.com', '483-485-4948')
sonny.print_contact_info()
sonny.add_friend(jordan)
print(sonny.friends)

it = Car('Infinity', 'Q50', '2017')
it.greet()
