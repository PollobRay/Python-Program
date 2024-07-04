from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget

Builder.load_file('check2.kv')

class MyLayout4(Widget):
    check=[]
    def checkbox_click(self, instance, value, topping): #topping is indicate which button checked
        if value :
            MyLayout4.check.append(topping)
            tops = ''
            for x in MyLayout4.check:
                tops = f'{tops} {x}'

            self.ids.output_label.text =f'you selected: {tops}'
            print(tops)
        else:
            MyLayout4.check.remove(topping)
            tops = ''
            for x in MyLayout4.check:
                tops = f'{tops} {x}'

            self.ids.output_label.text = f'you selected : {tops}'
            print(tops)


class MyApp(App):
    def build(self):
        return MyLayout4()


if __name__=='__main__':
    MyApp().run()



''''
#second technique in python file
class MyLayout4(Widget):
    check=[]



    def checkbox_click(self, instance, value, topping): #topping is indicate which button checked
            if value==True:
                MyLayout4.check.append(topping)
                tops=''
                for x in MyLayout4.check:
                    tops=f'{tops}{x}'

                self.ids.output_label.text=f'you selected: {tops}'

            else:
                MyLayout4.check.remove(topping)
                tops=''
                for x in MyLayout4.check:
                    tops=f'{tops}{x}'
                self.ids.output_label.text=f'you selected : {tops}'

class MyApp(App):
    def build(self, **kwargs):
        super().__init__(**kwargs)
        self.panel = BoxLayout()
        self.panel.orientation='vertical'


        self.head = Label()
        self.head.text = 'Select pizzza'
        self.panel.add_widget(self.head)
        
        self.grid = GridLayout()
        self.grid.cols = 2

        self.inner = Label()
        self.inner.text = "Inner 1"
        self.grid.add_widget(self.inner)
        self.inner2 = Label()
        self.inner2.text = "Inner 2"
        self.grid.add_widget(self.inner2)

        self.panel.add_widget(self.grid)
       
        self.footer = Label()
        self.footer.text= "Foother"
        self.panel.add_widget(self.footer)

        return self.panel

if __name__=='__main__':
    MyApp().run()

'''''