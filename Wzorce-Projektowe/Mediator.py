#Mediator

from __future__ import print_function

class User(object):
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator

    def send(self, message):
        mediator.ping(self.name, message)


class Mediator(object):
    def ping(self, name, message):
        print("Użytkownik {}: {}".format(name, message))

if __name__ == "__main__":
    mediator = Mediator()

    basia = User("Basia", mediator)
    kasia = User("Kasia", mediator)

    basia.send("Hej, co tam?")
    kasia.send("A dobrze, a u Ciebie?")