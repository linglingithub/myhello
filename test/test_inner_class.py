"""

In this example the constructor of the class Human (__init__) creates a new head object.

"""

class Human:
    def __init__(self):
        self.name = 'Guido'
        self.head = self.Head()
        self.brain = self.Brain()

    class Head:
        def talk(self):
            print("talk_self: ", self)
            return 'talking...'

    class Brain:
        def think(self):
            return 'thinking...'


if __name__ == '__main__':
    guido = Human()
    print(guido.name)
    print(guido.head.talk())
    print(guido.brain.think())
    print(guido,guido.brain)
    print(Human.Brain, guido.Brain)
    print(Human.Brain(), guido.Brain())