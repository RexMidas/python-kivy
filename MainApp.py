import kivy
kivy.require('1.0.6')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class MyApp(App):

    def build(self):
        layout = BoxLayout(padding=10)
        button = Button(text='My first button', background_color=(1,0,0,1))
        layout.add_widget(button)
        label = Label(text='Hello world, this works ... awesome')
        layout.add_widget(label)
        return layout


if __name__ == '__main__':
    MyApp().run()