"""
Module that draw a rectangle on the screen
The rectangle follows the mouse/touch position
"""
from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle

class Touch(Widget):
    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)
        with self.canvas:
            self.rect = Rectangle(pos=(0, 0), size=(100, 100))

    def on_touch_down(self, touch):
        self.rect.pos = touch.pos
    def on_touch_move(self, touch):
        self.rect.pos = touch.pos
    
class drawApp(App):
    def build(self):
        return Touch()

if __name__ == '__main__':
    drawApp().run()
