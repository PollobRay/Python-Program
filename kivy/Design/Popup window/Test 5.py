from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget

Builder.load_file('popup.kv')
class MyLayout(Widget):
    pass

class Pop(App):
    def build(self):
        return MyLayout()

if __name__=='__main__':
    Pop().run()