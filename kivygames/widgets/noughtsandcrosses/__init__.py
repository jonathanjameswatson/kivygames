from kivy.properties import DictProperty, AliasProperty

from kivygames.games.noughtsandcrosses import NoughtsAndCrosses
from kivygames.widgets import GameLayout


class NoughtsAndCrosses(GameLayout):
    gameFunction = NoughtsAndCrosses
    outputs = DictProperty({
        'Player': 1,
        'Error': '',
        'End': '',
        'Grid': [0] * 9
    })
    playerText = AliasProperty(lambda self: str(self.outputs['Player']), bind=['outputs'])
