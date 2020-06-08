from kivygames.noughtsandcrosses import NoughtsAndCrosses

def testGame():
    game = NoughtsAndCrosses(2, 0)
    io = game.send(None)
    while io != StopIteration:
        isInput = io[0]
        if isInput:
            inputName = io[1]
            inputType = io[2]
            response = eval(input(f'Input value {inputName} of type {inputType.__name__}: '))
            io = game.send(response)
        else:
            outputName = io[1]
            response = io[2]
            print(f'{outputName}: {response}')
            io = game.send(None)
