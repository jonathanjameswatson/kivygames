from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.app import App
from kivy.properties import ObjectProperty


class MainMenu(BoxLayout):
    gameLayout = ObjectProperty()

    def __init__(self, **kwargs):
        BoxLayout.__init__(self, **kwargs)
        self.app = App.get_running_app()
        self.gameLayout = self.app.gameLayouts[0]
        buttonGrid = self.ids["buttonGrid"]
        for i, gameLayout in enumerate(self.app.gameLayouts):
            button = Button(
                text=gameLayout.name,
                on_press=lambda sender, i=i: self.setGame(gameLayout),
            )
            buttonGrid.add_widget(button)

    def setGame(self, gameLayout):
        self.gameLayout = gameLayout

    def startGame(self, instance, players):
        self.app.root.current = type(self.gameLayout).__name__.lower()
        self.gameLayout.start(players)
