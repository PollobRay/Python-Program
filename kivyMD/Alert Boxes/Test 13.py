from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog


class MainApp(MDApp):
    dialog=None
    def build(self):
        self.theme_cls.theme_style='Light' #'Dark'
        self.theme_cls.primary_palette='BlueGray'

        return Builder.load_file('alert.kv')

    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog=MDDialog(
                title='Alert',
                #text='pretty neat',
                buttons=[
                    MDFlatButton(
                        text='cancel',
                        text_color=self.theme_cls.primary_color,
                        on_release=self.close_dialog
                    ),
                    MDRectangleFlatButton(
                        text='Yes',
                        text_color=self.theme_cls.primary_color,
                        on_release=self.neat_dialog
                    )
                ]
            )

        self.dialog.open()

    def close_dialog(self,obj):
        self.dialog.dismiss()

    def neat_dialog(self,obj):
        self.dialog.dismiss()
        self.root.ids.my_label.text='yes its'


if __name__=='__main__':
    MainApp().run()