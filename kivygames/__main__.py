from os import scandir, environ, name
from os.path import abspath, join
from importlib import import_module
from kivy.config import Config


Config.set("kivy", "window_icon", "kivygames/assets/icon.ico")

import kivy
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.resources import resource_add_path

kivy.require("1.11.1")

if name == "nt":
    import ctypes
    import tkinter

    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    root = tkinter.Tk()
    root.overrideredirect(1)
    root.withdraw()
    dpi = ctypes.windll.user32.GetDpiForWindow(root.winfo_id())
    scale = str(dpi / 96)
    root.destroy()
    environ["KIVY_METRICS_DENSITY"] = scale


def importAll():
    Builder.load_file(abspath(f"{__file__}/../style.kv"))
    importWidgets("widgets")
    gameLayouts = importWidgets("gamelayouts", True)
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
            gameLayouts.append(getattr(module, "layout")())
    return gameLayouts if returnLayouts else None


class KivyGamesApp(App):
    def __init__(self, gameLayouts, **kwargs):
        App.__init__(self, **kwargs)
        self.gameLayouts = gameLayouts

    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        self.title = "Kivy Games"


def run():
    resource_add_path(abspath(f"{__file__}/../assets"))
    gameLayouts = importAll()

    KivyGamesApp(gameLayouts=gameLayouts).run()


if __name__ == "__main__":
    run()
