from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.tabbedpanel import TabbedPanel

Builder.load_file('im.kv')

class MyLayout(Widget):
    pass

class AwesomeApp(App):
    def build(self):

        return MyLayout()

if __name__=='__main__':
    AwesomeApp().run()