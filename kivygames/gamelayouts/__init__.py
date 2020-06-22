from kivy.uix.boxlayout import BoxLayout
from kivy.properties import DictProperty


class GameLayout(BoxLayout):
    name = ""
    gameObject = None
    outputs = DictProperty({})

    def __init__(self, **kwargs):
        BoxLayout.__init__(self, **kwargs)
        self.game = self.gameObject()
        self.ended = False
        self.nextInput = (None, None)

    def start(self, players):
        self.send(players)

    def send(self, value=None):
        io = self.game.send(value)
        isInput = io[0]
        if isInput == StopIteration:
            self.ended = True
            return None
        elif isInput:
            self.nextInput = io[1:]
        else:
            outputName = io[1]
            outputValue = io[2]
            self.outputs[outputName] = outputValue
            self.send()

    def gameInput(self, name, object, value):
        if self.ended:
            return None

        if name == self.nextInput[0]:
            self.send(value)
