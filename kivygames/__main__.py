from os import scandir
from os.path import abspath, join
from importlib import import_module
from kivy.app import App
from kivy.lang.builder import Builder
import kivy

kivy.require('1.11.1')

def importKv():
    widgetsDir = abspath(f'{__file__}/../widgets')
    widgetDirs = (f for f in scandir(widgetsDir) if f.is_dir() and f.name != '__pycache__')
    for widgetDir in widgetDirs:
        Builder.load_file(join(widgetDir.path, 'widget.kv'))
        import_module(f'kivygames.widgets.{widgetDir.name}')

class KivyGamesApp(App):
    pass

if __name__ == '__main__':
    importKv()
    KivyGamesApp().run()
