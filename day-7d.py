# inheritance

class InvalidOperationError(Exception):
    pass


class Stream:
    def __init__(self):
        self.opened - False

    def open(self):
        if self.opened:
            raise InvalidOperationError(
                "cannot open the stream which is already open")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError(
                "cannot close the stream which is already closed")
        self.opened = False


class FileStream(Stream):
    def read(self):
        print("reading from a file")


class NetworkStream(Stream):
    def read(self):
        print("reading from a network")
