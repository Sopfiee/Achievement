from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

# класс приложения
class Achievement(MDApp):
    def build(self):
        return MDLabel(text="Hello, super hero", halign="center")

