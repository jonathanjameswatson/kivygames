from kivy.properties import ListProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior


class Cell(ButtonBehavior, Image):
    pass

marks = ['empty.png', 'nought.png', 'cross.png']


class NoughtsAndCrossesBoard(GridLayout):
    cellsProperty = ListProperty([0] * 9)

    def __init__(self, **kwargs):
        GridLayout.__init__(self, **kwargs)
        self.cells = []
        for i in range(9):
            cell = Cell(source=marks[0], on_press=lambda sender,
                          i=i: self.increase(i))
            self.add_widget(cell)
            self.cells.append(cell)

        self.bind(cellsProperty=lambda obj, value: self.updateCells())

    def updateCells(self):
        for i, cell in enumerate(self.cells):
            cell.source = marks[self.cellsProperty[i]]

    def increase(self, i):
        self.cellsProperty[i] = (self.cellsProperty[i] + 1) % 3
