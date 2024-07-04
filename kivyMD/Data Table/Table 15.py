
from kivy.metrics import dp
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable


class MainApp(MDApp):

    def build(self):
        screen = Screen()
        table=MDDataTable(
            size_hint=(0.9,0.6),
            pos_hint={'center_x':0.5,'center_y':0.5},
            #check=True,
            #use_pagination=True,
            rows_num=3,
            pagination_menu_height='600dp',
            #pagination_menu_pos='auto',
            background_color=[1,0,0,5],

            column_data=[
                ('First Name',dp(30)),
                ('Last Name',dp(30)),
                ('E-mail',dp(30)),
                ('Phone No',dp(30)),
            ],

            row_data=[
                ('john','elder','','0178'),
                ('mery','a',' ','0189')
            ]
        )

        table.bind(on_check_press=self.checked)
        table.bind(on_row_press=self.row_checked)
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"

        screen.add_widget(table)
        return screen

    def checked(self, instance_table, current_row):
        print(instance_table, current_row)

    def row_checked(self, instance_table, instance_row):
        print(instance_table, instance_row)


if __name__=='__main__':
    MainApp().run()




