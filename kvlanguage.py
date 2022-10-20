'''
Module that uses the kivy langauge design to:
1. Creates nested gridlayouts
2. Triggers a button click
3. Clear input text
4. Used kivy proterties(ObjectProperty) to pass id(property) from kv file to python file
'''
from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class myGrid(Widget):
    username = ObjectProperty(None)
    def btn(self):
        print('Hello ', self.username.text)
        self.username.text = ''
        self.password.text = ''

class gridLayoutApp(App):
    def build(self):
        return myGrid()

if __name__ == '__main__':
    gridLayoutApp().run()