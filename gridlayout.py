'''
Module that creates nested gridlayouts
Triggers a button click
And clears input text
'''

from kivy.app import App 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class myGrid(GridLayout):
    def __init__(self, **kwargs):
        super(myGrid, self).__init__(**kwargs)
        self.cols = 1
        self.inside_grid = GridLayout()
        self.inside_grid.cols = 2
        self.inside_grid.add_widget(Label(text='Username'))
        self.username = TextInput(multiline=False)
        self.inside_grid.add_widget(self.username)
        self.inside_grid.add_widget(Label(text='Password'))
        self.password = TextInput(multiline=False, password=True)
        self.inside_grid.add_widget(self.password)
        self.add_widget(self.inside_grid)

        self.submit = Button(text='Submit', font_size=24)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)
    
    def pressed(self, instance):
        print('Hello ', self.username.text)
        self.username.text = ''
        self.password.text = ''

class gridLayoutApp(App):
    def build(self):
        return myGrid()

if __name__ == '__main__':
    gridLayoutApp().run()