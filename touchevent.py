from kivy.app import App 
from kivy.uix.widget import Widget

class Touch(Widget):
    def on_touch_down(self, touch):
        print("Mouse Down", touch)

class touchEventApp(App):
    def build(self):
        return Touch()

if __name__ == '__main__':
    touchEventApp().run()