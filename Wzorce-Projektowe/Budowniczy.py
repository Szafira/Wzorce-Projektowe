# Budowniczy

class AdoptionOffer():

    def __init__(self):
        self.type = None
        self.name = None
        self.sex = None
        self.age = None
        self.size = None

    def __str__(self):
        return '{} | {} | {}'.format(self.type, self.name, self.sex, self.age, self.size)      

class AbstractBuilder():

    def __init__(self):
        self.adoption_offer = None

    def createNewAdoptionOffer(self):
        self.adoption_offer = AdoptionOffer()
 
class ConcreteBuilder(AbstractBuilder):
    def addType(self):
        self.adoption_offer.type = "Kot"
        
    def addName(self):
        self.adoption_offer.name = "Kitek"

    def addSex(self):
        self.adoption_offer.sex = "Samiec"

    def addAge(self):
        self.adoption_offer.age = "Młody"

    def addSize(self):
        self.adoption_offer.size = "Mały"
 
class Director():
    def __init__(self, builder):
        self._builder = builder

    def constructAdoptionOffer(self):
        self._builder.createNewAdoptionOffer()
        self._builder.addType()
        self._builder.addName()
        self._builder.addSex()
        self._builder.addAge()
        self._builder.addSize()
 
    def getAdoptionOffer(self):
        return self._builder.adoption_offer
 
concreteBuilder = ConcreteBuilder()
director = Director(concreteBuilder)
 
director.constructAdoptionOffer()
adoption_offer_1 = director.getAdoptionOffer()
print("Oferta Adopcji: ", adoption_offer_1)