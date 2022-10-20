"""
Module that creates a popup window
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup

class myWidget(Widget):
    def btn(self):
        show_pop()

class P(FloatLayout):
    pass

class PopupApp(App):
    def build(self):
        return myWidget()

def show_pop():
    show = P()
    popup_window = Popup(title="Popup Window", content=show, size_hint=(None, None), size=(400, 400))
    popup_window.open()

if __name__ == '__main__':
    PopupApp().run()