# Singleton

class Singleton:
    __instance__= None
    
    def __init__(self):
        if Singleton.__instance__ != None:
            raise Exception("Ta klasa jest singletonem")
        else:
            Singleton.__instance__ = self
    
    @classmethod
    def get_instance(cls):
        if not cls.__instance__:
            cls.__instance__ == cls()
        return cls.__instance__
    
if __name__ == "__main__":
        obj = Singleton()
        print(obj)
        
        obj2 = Singleton.get_instance()
        print(obj2)
        
        obj3= Singleton.get_instance()
        print(obj3)
        