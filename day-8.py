# polymorphism

from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("Text box")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


def draw(control):
    control.draw()


textbox = TextBox()
draw(textbox)

dropdownlist = DropDownList()
draw(dropdownlist)


def draw_all_controls(controls):
    for control in controls:
        control.draw()


print('*' * 15)
draw_all_controls([dropdownlist, textbox])
