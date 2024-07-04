from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.picker import MDDatePicker


class MyApp(MDApp):
    def build(self):
        return Builder.load_file('design.kv')

    def show_date_picker(self):
        date_dialog=MDDatePicker()
        date_dialog.open()
        date_dialog.bind(on_save=self.on_save,on_cencel=self.on_cancel)

    def on_save(self,instance,value,date_range):
        self.root.ids.date_label.text=str(value)

    def on_cancel(self,instance,value):
        self.root.ids.date_label.text='you cancel'

if __name__=='__main__':
    MyApp().run()