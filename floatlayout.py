"""
Module that uses floatlayout 
Floatlayout is best for mobile screens
"""

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

class floatLayoutApp(App):
    def build(self):
        return FloatLayout()

if __name__ == '__main__':
    floatLayoutApp().run()
