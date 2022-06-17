#Pamiatka

from time import sleep


class Memento(object):
    def __init__(self, state):
        self._state = state

    def restore_version(self):
        return self._state
    
class OS_update(object):
    _state = "0"

    def set_version(self, state):
        print("Aktualizacja do wersji: ", state)
        self._state = state

    def create_rollback(self):
        print("Tworzenie kopii zapasowej")
        for i in range(3):
            print(".", end=" ")
            sleep(1)
        print("\n")

        return Memento(self._state)

    def restore_saved_version(self, memento):
        self._state = memento.restore_version()
        print("Przywrocono wersje: ", self._state)

rollbacks = []

_os_update = OS_update()
_os_update.set_version("1.023")

_os_update.set_version("1.024")
rollbacks.append(_os_update.create_rollback())

_os_update.set_version("1.100")
rollbacks.append(_os_update.create_rollback())
_os_update.restore_saved_version(rollbacks[0])




