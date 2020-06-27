from kivygames.games import Game
from enum import Enum
from random import choice


emojis = ["✊", "✋", "✌"]


class Hand(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    def __str__(self):
        return self.name.capitalize()

    def emoji(self):
        return emojis[self.value - 1]


rules = {Hand.ROCK: Hand.SCISSORS, Hand.PAPER: Hand.ROCK, Hand.SCISSORS: Hand.PAPER}


class RockPaperScissors(Game):
    minPlayers = 1
    maxPlayers = 1
    hasAI = False

    def __init__(self):
        Game.__init__(self)

    async def game(self):
        playerHand = await self.getInput("Hand", Hand, 1)
        AIHand = choice(tuple(Hand))
        await self.sendOutput("PlayerHand", playerHand.emoji())
        await self.sendOutput("AIHand", AIHand.emoji())
        if playerHand == AIHand:
            await self.sendOutput("End", "It's a draw!")
        else:
            winner = 1
            if rules[playerHand] != AIHand:
                winner = 2
            await self.sendOutput("End", f"Player {winner} wins!")
        await self.end()
