from os import scandir
from os.path import abspath, join
from importlib import import_module
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.resources import resource_add_path
import kivy


kivy.require("1.11.1")


def importAll():
    importWidgets("widgets")
    gameLayouts = importWidgets("gamelayouts", True)
    Builder.load_file(abspath(f"{__file__}/../style.kv"))
    return gameLayouts


def importWidgets(dirName, returnLayouts=False):
    gameLayouts = []
    widgetsDir = abspath(f"{__file__}/../{dirName}")
    widgetDirs = (
        f for f in scandir(widgetsDir) if f.is_dir() and f.name != "__pycache__"
    )
    for widgetDir in widgetDirs:
        Builder.load_file(join(widgetDir.path, "widget.kv"))
        module = import_module(f"kivygames.{dirName}.{widgetDir.name}")
        if returnLayouts:
            gameLayouts.append(getattr(module, "layout"))
    return gameLayouts if returnLayouts else None


class KivyGamesApp(App):
    def __init__(self, gameLayouts, **kwargs):
        App.__init__(self, **kwargs)
        self.gameLayouts = gameLayouts

    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        self.title = "Kivy Games"


if __name__ == "__main__":
    gameLayouts = importAll()
    resource_add_path(abspath(f"{__file__}/../assets"))

    KivyGamesApp(gameLayouts=gameLayouts).run()
