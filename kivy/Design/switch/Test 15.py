from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.tabbedpanel import TabbedPanel

Builder.load_file('sw.kv')

class MyLayout(Widget):
    def switch_click(self,switchobj,value):
        if(value):
            self.ids.my_label.text="ON"
        else:
            self.ids.my_label.text = "OFF"

class AwesomeApp(App):
    def build(self):

        return MyLayout()

if __name__=='__main__':
    AwesomeApp().run()