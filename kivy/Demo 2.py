from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class SayHello(App):
    def build(self):
        self.window=GridLayout()
        self.window.cols=1
        self.window.size_hint=(0.6,0.7)
        self.window.pos_hint={'center_x':0.5,'center_y':0.5}
        self.window.add_widget(Image(source='C:\\Users\\Ray\\Desktop\\Bani archana samsad\\form.png'))
        self.greeting=Label(text='Name',font_size=30)
        self.window.add_widget(self.greeting)
        self.user=TextInput()
        self.window.add_widget(self.user)
        self.food=Label(text="Food")
        self.window.add_widget(self.food)
        self.btn=Button(text='Greet',bold=True,background_color='white')
        self.btn.bind(on_press=self.press)
        self.window.add_widget(self.btn)

        return self.window
    def press(self,instance):
        self.greeting.text="Hello "+self.user.text




if __name__=='__main__':
    SayHello().run()