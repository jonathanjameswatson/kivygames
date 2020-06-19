import numpy as np
from kivy.properties import DictProperty, AliasProperty

from kivygames.games.noughtsandcrosses import NoughtsAndCrosses
from kivygames.gamelayouts import GameLayout


class NoughtsAndCrosses(GameLayout):
    name = "Noughts and crosses"
    gameFunction = NoughtsAndCrosses
    outputs = DictProperty(
        {"Player": 1, "Error": "", "End": "", "Grid": np.zeros((3, 3))}
    )
    playerText = AliasProperty(
        lambda self: f'Player {self.outputs["Player"]}', bind=["outputs"]
    )
    cells = AliasProperty(
        lambda self: self.outputs["Grid"].flatten().tolist(), bind=["outputs"]
    )


layout = NoughtsAndCrosses
