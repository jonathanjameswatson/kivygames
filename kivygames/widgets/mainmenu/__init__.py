from kivy.uix.widget import Widget
from kivy.uix.button import Button


class MainMenu(Widget):
    def __init__(self, **kwargs):
        Widget.__init__(self, **kwargs)

    def build(self):
        self.addButtons()

    def addButtons(self):
        print(self.ids)
        grid = self.ids['grid']
        for i in range(9):
            button = Button(
                text='X'
            )
            grid.add_widget(button)
