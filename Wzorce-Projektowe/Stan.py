#Stan

class camera_settings(object):
    
    name = "settings"
    allowed=[]
    def switch_setting(self, state):
        if state.name in self.allowed:
            print (self,' zmieniono na ',state.name)        
            self.__class__ = state
        else:
            print ('Blad przy zmianie z : ',self,'na ',state.name)

    def __str__(self):
        return self.name

class auto(camera_settings):
    name = "Tryb automatyczny"
    allowed = ['Tryb manualny','Tryb portretowy','Tryb krajobrazu','Tryb sportu']

class manual(camera_settings):
    name = "Tryb manualny"
    allowed = ['Tryb automatyczny','Tryb portretowy','Tryb krajobrazu','Tryb sportu']

class portrait(camera_settings):
    name = "Tryb portretowy"
    allowed = ['Tryb automatyczny','Tryb manualny','Tryb krajobrazu','Tryb sportu']

class landscape(camera_settings):
    name = "Tryb krajobrazu"
    allowed = ['Tryb automatyczny','Tryb manualny','Tryb sportu','Tryb portretowy']

class sport(camera_settings):
    name = "Tryb sportu"
    allowed = ['Tryb automatyczny','Tryb manualny','Tryb portretowy','Tryb krajobrazu']

class camera(object):
    def __init__(self):
        self.state = auto()

    def change(self,state):
        self.state.switch_setting(state)

   
_camera = camera()
_camera.change(auto)
_camera.change(manual)
_camera.change(portrait)
_camera.change(landscape)
_camera.change(sport)