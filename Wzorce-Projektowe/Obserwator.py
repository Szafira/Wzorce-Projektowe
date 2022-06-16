class Publisher(object):
    users = set()

    def register(self, user):
        self.users.add(user)

    def unregister(self, user):
        self.users.discard(user)

    def send_notifications(self, message):
        for user in self.users:
            user.notify(message)

class Subscriber(object):

    def __init__(self, username):
        self.username = username

    def notify(self, message):
        print(self.username + ' otrzymał/a powiadomienie: ' + message)

publisher = Publisher()

julia = Subscriber('Julia')
klaudia = Subscriber('Klaudia')
publisher.register(julia)
publisher.register(klaudia)


publisher.send_notifications('Zaktualizowaliśmy stronę')
publisher.send_notifications('Dodano nowy post, który może Cię zainteresować!')