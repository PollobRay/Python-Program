from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup


class Grid_Layout_Demo(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows=2
        self.cols=1

        self.label1=Label(text='Please click')
        self.add_widget(self.label1)

        self.label2=Button(text="Click", background_color=(0,24,67,1), color=(0,0,0,1))
        self.label2.bind(on_press= self.responds)
        self.add_widget(self.label2)



    def responds(self,instance):
        print("Clicked")

class Demo(App):
    def build(self):
        return Grid_Layout_Demo()

if __name__=='__main__':
    Demo().run()
