"""
Module to test kivy after install
Uses the Label class to display some text
"""

from kivy.app import App
from kivy.uix.label import Label

class introApp(App):
    def build(self):
        return Label(text='Hello There!!!')

if __name__ == '__main__':
    introApp().run()
