from kivy.properties import ListProperty, NumericProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior


class Cell(ButtonBehavior, Image):
    pass


marks = ["empty.png", "nought.png", "cross.png"]


class NoughtsAndCrossesBoard(GridLayout):
    cellsProperty = ListProperty([0] * 9)
    playerProperty = NumericProperty(1)

    def __init__(self, **kwargs):
        GridLayout.__init__(self, **kwargs)
        self.register_event_type("on_choose")
        self.cells = []
        for i in range(9):
            cell = Cell(
                source=marks[0],
                on_press=lambda sender, i=i: self.dispatch(
                    "on_choose", (i // 3, i % 3)
                ),
            )
            self.add_widget(cell)
            self.cells.append(cell)

        self.bind(cellsProperty=lambda obj, value: self.updateCells())

    def updateCells(self):
        for i, cell in enumerate(self.cells):
            cell.source = marks[self.cellsProperty[i]]

    def on_choose(self, position):
        pass
