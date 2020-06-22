from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.app import App

from kivygames.widgets.mainmenu import MainMenu


class KivyGamesScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        ScreenManager.__init__(self, **kwargs)
        mainmenu = Screen(name="mainmenu")
        mainmenu.add_widget(MainMenu())
        self.add_widget(mainmenu)
        for gameLayout in App.get_running_app().gameLayouts:
            screen = Screen(name=type(gameLayout).__name__.lower())
            screen.add_widget(gameLayout)
            self.add_widget(screen)
        self.current = "mainmenu"
