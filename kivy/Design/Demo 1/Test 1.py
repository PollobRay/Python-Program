from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget

Builder.load_file('my.kv')

class MyGridLayout(Widget):
    def press(self):
        n=self.ids.name.text
        f=self.ids.food.text
        print(n,"  ",f)

class Visual(App):
    def build(self):
        return MyGridLayout()

if __name__=='__main__':
    Visual().run()
