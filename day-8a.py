# extending built in types

class Text(str):
    def duplicate(self):
        return self + self


string = Text('PYTHON')
print(string.lower())
print(string.duplicate())


class TrackableList(list):
    def append(self, object):
        print("Append called")
        super().append(object)


list = TrackableList()
print(list.append(1))
