from kivy.properties import (
    NumericProperty,
    ObjectProperty,
    BooleanProperty,
    AliasProperty,
)
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior


class PlayerSelector(BoxLayout):
    gameObject = ObjectProperty()
    numPlayers = NumericProperty(2)
    numAI = NumericProperty(1)
    minPlayers = NumericProperty(1)
    maxPlayers = NumericProperty(2)
    maxAI = NumericProperty(1)
    hasAI = BooleanProperty()

    numPlayersText = AliasProperty(
        lambda self: f"Number of players: {self.numPlayers:.0f}", bind=["numPlayers"]
    )
    numAIText = AliasProperty(
        lambda self: f"Number of AIs: {self.numAI:.0f}", bind=["numAI"]
    )

    def __init__(self, **kwargs):
        BoxLayout.__init__(self, **kwargs)
        self.register_event_type("on_choose")

    def on_gameLayout(self, instance, gameObject):
        self.minPlayers = gameObject.minPlayers
        self.maxPlayers = gameObject.maxPlayers
        self.numPlayers = gameObject.maxPlayers
        self.hasAI = gameObject.hasAI
        if self.hasAI:
            self.maxAI = self.maxPlayers - 1
            self.numAI = self.maxPlayers - 1

    def submit(self):
        players = []
        numAI = self.numAI if self.hasAI else 0
        players += [False] * int(self.numPlayers - numAI)
        players += [True] * int(numAI)
        self.dispatch("on_choose", tuple(players))

    def on_choose(self, players):
        pass
