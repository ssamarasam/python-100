print("arithmetic initialized", __name__)


def divide():
    pass


def sum():
    pass


if __name__ == "__main__":
    print("arithmetic started")
    divide()


# if we import this moduel into another mopdule and execuet this code, the above priece of code wont work as the name wll change from __main__ to arithmetic
