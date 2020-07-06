from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import DictProperty

from kivygames.widgets.emojibutton import EmojiButton


class GameLayout(BoxLayout):
    name = ""
    gameObject = None
    outputs = DictProperty({})

    def __init__(self, **kwargs):
        BoxLayout.__init__(self, **kwargs)
        self.players = None
        self.initialOutputs = self.outputs.copy()
        self.initialise()
        controls = FloatLayout(size_hint=(1, 0.2))
        back = EmojiButton(
            text="◀",
            size_hint=(None, 0.8),
            pos_hint={"center_x": 0.25, "center_y": 0.5},
            on_press=lambda _: self.back(),
        )
        restart = EmojiButton(
            text="🔄",
            size_hint=(None, 0.8),
            pos_hint={"center_x": 0.75, "center_y": 0.5},
            on_press=lambda _: self.restart(),
        )
        controls.add_widget(back)
        controls.add_widget(restart)
        self.add_widget(controls)

    def initialise(self):
        self.outputs = self.initialOutputs.copy()
        self.game = self.gameObject()
        self.ended = False
        self.nextInput = (None, None)

    def start(self, players):
        self.players = players
        self.send(self.players)

    def restart(self):
        self.initialise()
        self.start(self.players)

    def back(self):
        self.initialise()
        App.get_running_app().root.current = "mainmenu"

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
