from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.window import Window
Window.size = (400, 240)

class safe(App):
    password = ''
    passtry = ''
    open = False
    doorOpen = False

    bg = None

    def Draw(self, img):
        self.bg.source = img

    # region Digits Funcs
    def d1Pressed(self, event):
        self.passtry += '1'

    def d2Pressed(self, event):
        self.passtry += '2'

    def d3Pressed(self, event):
        self.passtry += '3'

    def d4Pressed(self, event):
        self.passtry += '4'

    def d5Pressed(self, event):
        self.passtry += '5'

    def d6Pressed(self, event):
        self.passtry += '6'

    def d7Pressed(self, event):
        self.passtry += '7'

    def d8Pressed(self, event):
        self.passtry += '8'

    def d9Pressed(self, event):
        self.passtry += '9'

    def d0Pressed(self, event):
        self.passtry += '0'
    # endregion

    def tryPass(self, event):
        print(self.password)
        if self.passtry == self.password:
            self.open = True
            self.Draw('SafeUnl.png')
        else:
            self.open = False

        self.passtry = ''

    def changePass(self, event):
        print(self.passtry)
        if self.doorOpen:
            self.password = self.passtry

    def openDoor(self, event):
        if not (self.open): return

        self.doorOpen = True
        self.Draw('SafeOp.png')

    def closeDoor(self, event):
        if not (self.doorOpen): return

        self.doorOpen = False
        self.open = False
        self.Draw('Safe.png')
        self.passtry = ''

    def build(self):
        main_layout = FloatLayout(height='100', width='100')
        self.password = '1111'
        self.bg = Image(source='Safe.png')
        main_layout.add_widget(self.bg)

        button1 = Button(text="", pos=(24, 212), size_hint=(0.09, 0.15), size=(8, 8), background_color=(0,0,0,0))
        button1.bind(on_press=self.d1Pressed)
        button2 = Button(text="", pos=(79, 212), size_hint=(0.09, 0.15), size=(8, 8), background_color=(0,0,0,0))
        button2.bind(on_press=self.d2Pressed)
        button3 = Button(text="", pos=(134, 212), size_hint=(0.09, 0.15), size=(8, 8), background_color=(0,0,0,0))
        button3.bind(on_press=self.d3Pressed)
        button4 = Button(text="", pos=(24, 157), size_hint=(0.09, 0.15), size=(8, 8), background_color=(0,0,0,0))
        button4.bind(on_press=self.d4Pressed)
        button5 = Button(text="", pos=(79, 157), size_hint=(0.09, 0.15), size=(8, 8), background_color=(0,0,0,0))
        button5.bind(on_press=self.d5Pressed)
        button6 = Button(text="", pos=(134, 157), size_hint=(0.09, 0.15), size=(8, 8), background_color=(0,0,0,0))
        button6.bind(on_press=self.d6Pressed)
        button7 = Button(text="", pos=(24, 102), size_hint=(0.09, 0.15), size=(8, 8), background_color=(0,0,0,0))
        button7.bind(on_press=self.d7Pressed)
        button8 = Button(text="", pos=(79, 102), size_hint=(0.09, 0.15), size=(8, 8), background_color=(0,0,0,0))
        button8.bind(on_press=self.d8Pressed)
        button9 = Button(text="", pos=(134, 102), size_hint=(0.09, 0.15), size=(8, 8), background_color=(0,0,0,0))
        button9.bind(on_press=self.d9Pressed)
        button0 = Button(text="", pos=(24, 47), size_hint=(0.09, 0.15), size=(8, 8), background_color=(0,0,0,0))
        button0.bind(on_press=self.d0Pressed)
        buttonr = Button(text="", pos=(79, 47), size_hint=(0.09, 0.15), size=(8, 8), background_color=(0,0,0,0))
        buttonr.bind(on_press=self.tryPass)
        buttone = Button(text="", pos=(134, 47), size_hint=(0.09, 0.15), size=(8, 8), background_color=(0,0,0,0))
        buttone.bind(on_press=self.changePass)
        buttond = Button(text="", pos=(194, 47), size_hint=(0.36, 0.7), size=(8, 8), background_color=(0,0,0,0))
        buttond.bind(on_press=self.openDoor)
        buttonc = Button(text="", pos=(380, 47), size_hint=(0.1, 0.7), size=(8, 8), background_color=(0,0,0,0))
        buttonc.bind(on_press=self.closeDoor)

        main_layout.add_widget(button1)
        main_layout.add_widget(button2)
        main_layout.add_widget(button3)
        main_layout.add_widget(button4)
        main_layout.add_widget(button5)
        main_layout.add_widget(button6)
        main_layout.add_widget(button7)
        main_layout.add_widget(button8)
        main_layout.add_widget(button9)
        main_layout.add_widget(button0)
        main_layout.add_widget(buttonr)
        main_layout.add_widget(buttone)
        main_layout.add_widget(buttond)
        main_layout.add_widget(buttonc)
        return main_layout

if __name__ == "__main__":
    safe().run()