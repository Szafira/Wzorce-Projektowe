#Metoda Szablonowa

class Pancakes:
    
    def make_pancakes(self):
       self.add_ingredients() 
       self.add_main_ingredient()
       self.mix_ingredients()
       self.fry()
       self.add_extras()
       self.serve()

    def add_ingredients(self):
        print("Do miski wrzuć składniki: szklanka mąki, jedno jajko, szklanka mleka, pół szklanki oleju")
    def add_main_ingredient(self):
        pass
    def mix_ingredients(self): 
        print("Wymieszaj wszystkie składniki razem")   
    def fry(self):
        print("Smaż na dobrze rozgrzanej patelni")
    def add_extras(self):
        pass
    def serve(self):
        print("Twoje naleśniki są gotowe, smacznego!")
   

class ChocolatePancakes(Pancakes):

    def add_main_ingredient(self):
        print("Dodaj dwie łyżki kakao oraz dwie łyżki cukru")
    def add_extras(self):
        print("Posmaruj dżemem porzeczkowym") 

    
class ChickenPancakes(Pancakes):

    def add_main_ingredient(self):
        print("Dodaj dwie łyżki soli")
    def add_extras(self):
        print("Dodaj usmażanego kurczaka, warzywa oraz ulubiony sos") 
        
class FruitPancakes(Pancakes):

    def add_main_ingredient(self):
        print("Dodaj dwie łyzki cukru")
    def add_extras(self):
        print("Udekoruj ulubionym owocami oraz bitą śmietaną") 

print("Naleśniki czekoladowe z dżemem porzeczkowym")
chocolatepancakes = ChocolatePancakes()
chocolatepancakes.make_pancakes()
print("\n")
print("Wytrawne naleśniki z kurczakiem")
chickenpancakes = ChickenPancakes()
chickenpancakes.make_pancakes()
print("\n")
print("Naleśniki z owocami oraz bitą śmietaną")
fruitpancakes = FruitPancakes()
fruitpancakes.make_pancakes()