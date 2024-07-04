from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget

Builder.load_file('designpop.kv')
''''
class Windgets(Widget):
    def show_popup(self):
        showp = self.PopWidget(self)
        popupWindow = Popup(title="Popup", content=showp, size_hint=(None, None), size=(400, 400))
        popupWindow.open()

    def btn(self):
        self.show_popup()
    def dumy(self):
        print('hello')

    class PopWidget(GridLayout):
        def __init__(self, outer):
            self.outer = outer

        def press_btn(self):
            print("Clicked")
            print(self.ids.inputT.text)
            #ids.superlabel.text='roy'
            #Windgets.root.ids.superlabel.text='roy'
            #app.ids.superlabel.text='roy'
            self.outer.dumy()



'''
class Windgets(Widget):
    def show_popup(self):
        showp = self.dumy(self)
        popupWindow = Popup(title="Schedule class", content=showp, size_hint=(None, None), size=(400, 400))
        popupWindow.title_align='center'
        popupWindow.title_color='#d82f05'
        popupWindow.title_size='26sp'
        popupWindow.open()

    def btn(self):
        self.show_popup()
        #print(name)

    def dumy(self,obj):
        class PopWidget(GridLayout):

            def press_btn(self,iid):
                print("Clicked")
                print(self.ids.teachers.text)
                print(self.ids.inputT.text) #access class memeber
                obj.ids.superlabel.text=self.ids.inputT.text #access outerclass member
                print('Hr ',iid.text) #accress by id
        return PopWidget()


class MyApp(App):
    def build(self):
        return Windgets()


if __name__=='__main__':
    MyApp().run()