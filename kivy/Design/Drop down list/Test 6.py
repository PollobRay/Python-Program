from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget

Builder.load_file('droplist.kv')

class MyLayout(Widget):
    def spinner_clicked(self,value):
        self.ids.click_label.text=f'You selected {value}'

class MyApp(App):
    def build(self):
        return MyLayout()

if __name__=='__main__':
    MyApp().run()
