__version__ = "1.0.0" 

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout



class HelloWorldApp(App):
    def build(self):
        self.box = BoxLayout(orientation='vertical')
        self.label = Label(text='text')

        self.button = Button(text='click me!')
        self.button.bind(on_press=self.on_button_press)
        
        self.box.add_widget(self.label)
        self.box.add_widget(self.button)
        
        return self.box

    def on_button_press(self, instance):
        self.label.text = 'Hello World'

if __name__ == '__main__':
    HelloWorldApp().run()
