from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget

Builder.load_file('ev.kv')

class MyLayout(Widget):
    def set_focus(self,obj,value):
        if(value=='down'):
            print("pressed")
        elif(value=='up'):
            print("Up")
        else:
            print("Move")
        self.ids.texti.focus = True

class MyApp(App):
    def build(self):
        return MyLayout()

if __name__=='__main__':
    MyApp().run()