import kivy
kivy.require('1.0.6')

from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):

    def build(self):
		layout = BoxLayout(padding=10)
		button = Button(text='My first button')
		layout.add_widget(button)
        return Label(text='Hello world, this works ... awesome')


if __name__ == '__main__':
    MyApp().run()