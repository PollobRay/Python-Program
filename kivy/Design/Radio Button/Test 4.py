from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget

Builder.load_file('radio.kv')


class MyLayout4(Widget):
    check = []

    def checkbox_click(self, instance, value, topping):  # topping is indicate which button checked
        if value:
            MyLayout4.check.append(topping)
            tops = ''
            for x in MyLayout4.check:
                tops = f'{tops} {x}'

            self.ids.output_label.text = f'you selected: {tops}'
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


if __name__ == '__main__':
    MyApp().run()

