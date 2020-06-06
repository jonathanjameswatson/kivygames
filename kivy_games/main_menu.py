from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class MainMenu(GridLayout):

    def __init__(self, **kwargs):
        GridLayout.__init__(self, **kwargs)
        self.cols = 1
        self.add_widget(Label(text='Welcome!'))
