#Iterator

class Pet:

    def __init__(self, name, type, race):
        self.name = name
        self.type = type
        self.race = race

    def __str__(self):
        return " {}  to {} o rasie {}".format(self.name, self.type, self.race)

class PetsIterator:
    def __init__(self, pets):
        self.index = 0
        self.pets = pets

    def has_next(self):
        if self.index >= len(self.pets):
            return False
        return True

    def next(self):
        pet = self.pets[self.index]
        self.index += 1
        return pet

if __name__ == '__main__':
    pet1 = Pet('Lucek', 'kot', 'kot perski')
    pet2 = Pet('Aleks', 'pies', 'owczarek niemiecki')
    pet3 = Pet('Miki', 'pies', 'chihuahua')
    pet4 = Pet('Rudzik', 'kot', 'kot brytyjski')
    pets = []
    pets.append(pet1)
    pets.append(pet2)
    pets.append(pet3)
    pets.append(pet4)

    iterator = PetsIterator(pets)

    while iterator.has_next():
        pet = iterator.next()
        print(pet)