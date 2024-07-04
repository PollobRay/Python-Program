from kivy.animation import Animation
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget

Builder.load_file('amin.kv')

class MyLayout(Widget):
    def animate_it(self,widget,*args):
        animate=Animation(background_color=(0,0,0,1),duration=1)
        animate+=Animation(size_hint=(1,1))
        animate+=Animation(size_hint=(0.5,0.5))
        animate+=Animation(pos_hint={'center_x':0.1})
        animate+=Animation(pos_hint={'center_y':0.5})
        animate.start(widget)
        animate.bind(on_complete=self.my_callback)


class MyApp(App):
    def build(self):
        return MyLayout()

if __name__=='__main__':
    MyApp().run()