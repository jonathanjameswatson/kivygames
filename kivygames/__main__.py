import asyncio
from os import scandir
from os.path import abspath, join
from importlib import import_module
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.resources import resource_add_path
import kivy


kivy.require('1.11.1')


def importKv():
    widgetsDir = abspath(f'{__file__}/../widgets')
    widgetDirs = (f for f in scandir(widgetsDir)
                  if f.is_dir() and f.name != '__pycache__')
    for widgetDir in widgetDirs:
        Builder.load_file(join(widgetDir.path, 'widget.kv'))
        import_module(f'kivygames.widgets.{widgetDir.name}')
    Builder.load_file(abspath(f'{__file__}/../style.kv'))


class KivyGamesApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        self.title = 'Kivy Games'

    def app_func(self):
        async def run_wrapper():
            await self.async_run()

        return asyncio.gather(run_wrapper())


if __name__ == '__main__':
    importKv()
    resource_add_path(abspath(f'{__file__}/../assets'))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(KivyGamesApp().app_func())
    loop.close()
    KivyGamesApp().run()
