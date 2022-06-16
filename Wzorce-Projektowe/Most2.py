#Most

class Desc:
   
    def pet(self, type, sex, size):
        print(f'Ten zwierzak to {type}, jest to {sex}  i jest {size} wielkości')

  
class Pet:
  
    def __init__(self, type, sex, size, desc):
        self._type = type
        self._sex = sex
        self._size = size
        self.desc = desc
  
    def create(self):
        self.desc.pet(self._type, self._sex, self._size)
  
    def expand(self, times):
        self._type = self._type * times
        self._sex = self._sex * times
        self._size = self._size * times

pet1 = Pet("kot", "samiec", "średniej", Desc())
pet1.create()
  
pet2 = Pet("pies", "samica", "dużej", Desc())
pet2.create()