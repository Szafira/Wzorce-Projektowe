
## Fasada
from itertools import repeat
import random
from time import sleep

class Cat:
    def __init__(self):
        self.rest = Rest()
        self.food = Food()
        self.play = Play()

    def Day(self):
        print("New day!")
        self.rest.Sleep_on_couch()
        self.food.Check_the_bowl()
        self.food.Meow_for_food()
        self.food.Meow_for_food()
        self.play.Play_with_toys()
        self.play.Play_with_food()
        self.play.Run_around
        self.food.Meow_for_food()
        self.rest.Sleep_on_cat_bed()

    def Night(self):
        self.play.Play_with_random()
        self.rest.Sleep_on_couch()
        self.play.Play_with_random()
        self.play.Run_around()
        self.rest.Sleep_on_bed()
    
class Rest:
    def Sleep_on_couch(self):
        print("Sleeping on couch")
        sleep(1)
        print("Zzz")

    def Sleep_on_bed(self):
        print("Sleeping on bed")
        sleep(1)
        print("Zzz")

    def Sleep_on_cat_bed(self):
        print("Sleeping on cat bed")
        sleep(1)
        print("Zzz")
                
        
class Food:
    def Check_the_bowl(self):
        print("Check the bowl")
        sleep(1)
        print("It is not full!")

    def Eat(self):
        print("Eating")
        sleep(1)
        
    def Meow_for_food(self):
        print("Meow")
        sleep(1)
        print("Meow")

class Play:
    def Play_with_toys(self):
        print("Playing with rubber ducky")

    def Play_with_food(self):
        print("Playing with food")
        
    def Play_with_random(self):
        x = random.randint(0, 4)
        if(x==0):
            print("Play with paper")
        elif(x==1):
            print("Play with screwdriver")
        elif(x==2):
            print("Play with pen")
        elif(x==3):
            print("Chase the fly ")
    
    def Run_around(self):
        print("Running around!")

cat = Cat()
cat.Day()
cat.Night()
