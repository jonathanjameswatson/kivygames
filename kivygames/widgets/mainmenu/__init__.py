from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.app import App


class MainMenu(BoxLayout):
    def __init__(self, **kwargs):
        BoxLayout.__init__(self, **kwargs)
        buttonGrid = self.ids["buttonGrid"]
        self.app = App.get_running_app()
        for i, gameLayout in enumerate(self.app.gameLayouts):
            button = Button(
                text=gameLayout.name,
                on_press=lambda sender, i=i: self.setGame(gameLayout),
            )
            buttonGrid.add_widget(button)

    def setGame(self, gameLayout):
        self.app.root.current = gameLayout.__name__.lower()
