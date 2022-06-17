#Adapter 

class distance:
    def get_distance(self):
        return 161

class USA_distance:
    def show_distance(self,x):
        print("Remaining: {} miles".format(x))

class unit_adapter:
    def __init__(self):
        unit_adapter._usa_distance = USA_distance()
        unit_adapter._distance = distance()

    def change_unit(self):
        x = self._distance.get_distance()
        x= x*0.6214
        self._usa_distance.show_distance(x)


_unit_adapter = unit_adapter()
_unit_adapter.change_unit()
