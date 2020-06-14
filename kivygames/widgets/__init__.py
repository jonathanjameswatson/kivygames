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
    outputs = DictProperty()

    def __init__(self, **kwargs):
        BoxLayout.__init__(self, **kwargs)
        self.game = self.gameFunction(2, 0)
        '''io = game.send(None)
        while io != StopIteration:
            isInput = io[0]
            if isInput:
                inputName = io[1]
                inputType = io[2]
                response = eval(
                    input(f'Input value {inputName} of type {inputType.__name__}: '))
                io = game.send(response)
            else:
                outputName = io[1]
                response = io[2]
                print(f'{outputName}: {response}')
                io = game.send(None)'''
