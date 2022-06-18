#Pelnomocnik

class database_server:
    def show_files(self):
        print("Status serwera:")
        print("OS: Windows 11 Nickel | Czas dzialania: 25h 32 min ")

class proxy:
    def __init__(self):
        self.auth = False
        self.show_file = None

    def show_files_auth(self):
        print("Podaj haslo")
        password = input()
        if(password == 'auth'):
            self.auth = True
            print('Zalogowano')
        else: 
            print("Nieprawidlowe haslo!")

    def show_files(self):
        if(self.auth == True):
            self._database_server = database_server()
            self._database_server.show_files()
        else:
            print("Zaloguj sie by sprawdzic dane")

_proxy = proxy()
print("Podaj co chcesz zrobic?")
print("Zaloguj | Sprawdz status | Zakoncz")
while True:
    input1 = input()
    if(input1=="Zaloguj"):
        while _proxy.auth == False:
            _proxy.show_files_auth()

    if(input1=="Sprawdz status"):
        _proxy.show_files()

    if input1 == "Zakoncz":
        break
