from kivy.uix.label import Label
from kivy.app import App
import kivy
kivy.require('1.11.1')


class Main(App):
    def build(self):
        return Label(text='Testing')


if __name__ == '__main__':
    Main().run()
