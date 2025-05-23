# polymorphism

from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod  # defining common behaviour for the children
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("Text box")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


# as long as the control has draw method, it will work, so the TedxtBox or DropdownList clasees need not be inherited from UIControl
# it just need to have draw method for the below function to work at run time
# duck typing - if it walks like a duck and talks like duck
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
