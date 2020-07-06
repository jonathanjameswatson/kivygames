from kivy.properties import DictProperty

from kivygames.games.rockpaperscissors import RockPaperScissors, Hand
from kivygames.widgets.emojibutton import EmojiButton
from kivygames.gamelayouts import GameLayout


class HandButton(EmojiButton):
    def select(self, number):
        self.parent.parent.parent.parent.gameInput("Hand", self, Hand(number))


class RockPaperScissors(GameLayout):
    name = "Rock, Paper, Scissors"
    gameObject = RockPaperScissors
    outputs = DictProperty({"PlayerHand": "", "AIHand": "", "End": ""})


layout = RockPaperScissors
