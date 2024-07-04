from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget

Builder.load_file('multiple.kv')

class MyLayout1(Widget):
    def checkbox_click(self, instance,value):
        print("Checked : ",value)

class Demo(App):
    def build(self):
        return MyLayout1()

if __name__=='__main__':
    Demo().run()
