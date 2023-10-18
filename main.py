from kivy.app import App
from kivy.uix.screenmanager import Screen
import random
import math

image = ""



class DisplayFrameApp(App):
    pass


class Display(Screen):
    def getImage(self):
        self.ids.imageName.source = self.ids.textInput.text
    def loadImage(self):
        return image



DisplayFrameApp().run()