# Strategia

class WatchingTheSeries:
    def __init__(self, func=None):
        if func:
             self.watch = func

    def watch(self):
        print("Oglądanie serialu na telewizorze")

def watch_on_laptop():
    print("Oglądanie serialu na laptopie")

def watch_on_phone():
    print("Oglądanie serialu na telefonie")

if __name__ == "__main__":
    strategia0 = WatchingTheSeries()
    strategia1 = WatchingTheSeries(watch_on_laptop)
    strategia2 = WatchingTheSeries(watch_on_phone)

    strategia0.watch()
    strategia1.watch()
    strategia2.watch()