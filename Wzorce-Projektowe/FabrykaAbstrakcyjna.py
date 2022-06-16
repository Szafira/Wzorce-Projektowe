# Fabryka abstrakcyjna

from abc import ABC, abstractmethod

    
class Dog(ABC):
       @abstractmethod
       def adoption(self):
        pass
    
class PureBreedDog(Dog):
        def adoption(self):
            return "Adoptowałeś Psa Rasowego!"
        
class NonPureBreedDog(Dog):
        def adoption(self):
            return "Adoptowałeś Psa Nierasowego!"
 
        
class Cat(ABC):
       @abstractmethod
       def adoption(self):
         pass
    
class PureBreedCat(Cat):
        def adoption(self):
            return "Adoptowałeś Kota Rasowego!"
        
class NonPureBreedCat(Cat):
        def adoption(self):
            return "Adoptowałeś Kota Nierasowego!"
    
class Pets(ABC):
    @abstractmethod
    def create_dog(self):
        pass
    @abstractmethod
    def create_cat(self):
        pass
    
class PureBreedPets(Pets):
    def create_dog(self):
        return PureBreedDog()
    
    def create_cat(self):
        return PureBreedCat()
    
class NonPureBreedPets(Pets):
    def create_dog(self):
        return NonPureBreedDog()
    
    def create_cat(self):
        return NonPureBreedCat()
    
if __name__ == "__main__":
    type = PureBreedPets()
    cat = type.create_cat()
    print(cat.adoption())
    
    