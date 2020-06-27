from kivygames.games.rockpaperscissors import RockPaperScissors, Hand


def testGame():
    game = RockPaperScissors()
    io = game.send([False])
    while io[0] != StopIteration:
        isInput = io[0]
        if isInput:
            inputName = io[1]
            inputType = io[2]
            response = eval(
                input(f"Input value {inputName} of type {inputType.__name__}: ")
            )
            response = inputType(response)
            io = game.send(response)
        else:
            outputName = io[1]
            response = io[2]
            print(f"{outputName}: {response}")
            io = game.send(None)
