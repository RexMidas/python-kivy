import kivy
kivy.require('1.0.6')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scatter import Scatter


class MyApp(App):

    def build(self):
        layout = BoxLayout(padding=10)
        scatter = Scatter()
        button = Button(text='My first button', background_color=(1,0,0,1))
        layout.add_widget(button)
        label = Label(text='Hello world, this works ... awesome')
        scatter.add_widget(label)
        layout.add_widget(scatter)
        return layout


if __name__ == '__main__':
    MyApp().run()