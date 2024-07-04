from kivy.uix.widget import Widget
from kivymd.app import MDApp


class MyLayout(Widget):
    pass
class AwesomeApp(MDApp):
    def build(self):
        return MyLayout()