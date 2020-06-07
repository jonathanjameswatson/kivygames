from kivy.app import App
import kivy

from kivy_games.gui.main_menu import MainMenu

kivy.require('1.11.1')


class Main(App):
    def build(self):
        return MainMenu()

if __name__ == '__main__':
    Main().run()
