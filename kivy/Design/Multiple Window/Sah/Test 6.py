from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


#Define our different screens
class FirstWindow(Screen):
	pass

class CourseCo(Screen):
	pass

class WindowManager(ScreenManager):
	pass

#kv = Builder.load_file('window.kv')

class AwesomeApp(MDApp):
	def build(self):
		return Builder.load_file('window.kv')

if __name__ == '__main__':
	AwesomeApp().run()