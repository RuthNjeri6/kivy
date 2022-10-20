"""
Module that creates multiple screen
with buttons to navigate from one screen to the next
after some validation
"""

from kivy.app import App 
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class LoginWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class myMainApp(App):
    def build(self):
        return Builder.load_file('screens.kv')

if __name__ == '__main__':
    myMainApp().run()