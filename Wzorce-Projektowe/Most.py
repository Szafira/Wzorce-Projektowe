# Most

from abc import ABC, abstractmethod

class Pet(ABC):
    def __init__(self, size):
        #self.sex = sex
        self.size = size
        
    @abstractmethod
    def display(self):
        pass
    
    #def display_sex(self):
       # self.sex.get_sex()
    
    def display_size(self):
        self.size.get_size()
    
class Cat(Pet):
    def display(self):
        print("Kot")
        
class Dog(Pet):
    def display(self):
        print("Pies")
        
    
#class Sex(ABC):
  #  @abstractmethod
   # def get_sex(self):
    #    pass

#class Female(Sex):
    #   def get_sex(self):
       #    print("Płeć : Samica")
        
 #  class Male(Sex):
     #  def get_sex(self):
        #  # print("Płeć: Samiec")
        
        
class Size(ABC):
    @abstractmethod
    def get_size(self):
        pass
    
  
class Small(Size):
    def get_size(self):
        print("Wielkość: mały")

class Medium(Size):
    def get_size(self):
        print("Wielkość: średni")
        
class Big(Size):
    def get_size(self):
        print("wielkość: duży")
        

#female = Female()
#male = Male()
small = Small()
medium = Medium()
small_cat = Cat(small)
#male_dog = Dog(male)

small_cat.display()
small_cat.display_size()



        
    
    
        
        