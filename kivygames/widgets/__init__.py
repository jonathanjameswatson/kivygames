from inspect import currentframe
from os import extsep
from os.path import splitext, exists
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import DictProperty


def loadKv():
    filename = currentframe().f_back.f_code.co_filename
    f = extsep.join((splitext(filename)[0], 'kv'))
    if exists(f) and f not in Builder.files:
        Builder.load_file(f)


class GameLayout(BoxLayout):
    gameFunction = None
    outputs = DictProperty({})

    def __init__(self, **kwargs):
        BoxLayout.__init__(self, **kwargs)
        self.game = self.gameFunction(2, 0)
        self.ended = False
        self.nextInput = (None, None)
        self.send()

    def send(self, value=None):
        io = self.game.send(value)
        if io == StopIteration:
            self.ended = True
            return None

        isInput = io[0]
        if isInput:
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
