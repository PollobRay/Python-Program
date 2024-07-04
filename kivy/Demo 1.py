from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput


class Kivy_UI(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.rows = 4

        self.myImg = Image(source='C:\\Users\\Ray\\Desktop\\Bani archana samsad\\form.png')
        self.add_widget(self.myImg)

        self.lab1 = Label(text="Name")
        self.add_widget(self.lab1)

        self.txt = TextInput(text='', font_size=40)
        self.add_widget(self.txt)

        self.btn = Button(text='Submit')
        self.btn.bind(on_press=self.btnRes)
        self.add_widget(self.btn)

        self.pop = Popup(title='Pop up window', size_hint=(0.4, 0.4), auto_dismiss=True,content=Label(text=""))

    def btnRes(self, element):
        self.pop.content.text = self.txt.text
        self.btn.text="clicked"
        self.pop.open()
        print("Clicked")


class DemuProgram(App):
    def build(self):
        return Kivy_UI()


if __name__ == '__main__':
    DemuProgram().run()
