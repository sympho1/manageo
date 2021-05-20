from kivy.uix.widget import Widget
from kivy.uix.behaviors import ButtonBehavior
from kivy.lang import Builder

class Btn(ButtonBehavior, Widget):
    pass

kv = """  
<Btn>:
    text: "Valider"
    color: (.8, .5, .3, 1)
    canvas.before:
        PushMatrix:
        Scale:
            origin: self.center
            x: 0.85 if self.state == "down" else 1
    canvas.after:
        PopMatrix

    canvas:
        Color:
            rgba: root.color
        RoundedRectangle:
            pos: self.pos
            size: self.size
    Label:
        text: root.text
        center: root.center
"""

Builder.load_string(kv)