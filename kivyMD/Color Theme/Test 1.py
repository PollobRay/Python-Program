from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivymd.app import MDApp


class AwesomeApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette='Blue'
        self.theme_cls.accent_palette='Red'
        return Builder.load_file('color.kv')

if __name__=='__main__':
    AwesomeApp().run()