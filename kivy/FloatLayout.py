from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout


class Float_Layout(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.btn1=Button(text="Button 1",
                         size_hint=(0.4,0.4),
                         pos_hint={'x':0.3,'y':0.2})
        self.add_widget(self.btn1)

        self.btn2 = Button(text="Button 2",
                           size_hint=(0.1, 0.2),
                           pos_hint={'x': 0.9, 'y': 0.8})
        self.add_widget(self.btn2)



class Demo2(App):
    def build(self):
        return Float_Layout()


if __name__=='__main__':
    Demo2().run()