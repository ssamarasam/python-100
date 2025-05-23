# Abstract Base class

# when we have a base class and sub classes whcih are inherited from base class
# and when we instanctiate a object from the base class, it is invalid
# for example Animal is base, and sub classes are fish and bird
# the right way to instantiate is from bird and fish classes as they are valid and specifies which animal is that
# instantiating form animal class like xyz = Animal is invalid as it misses what type of animal it is
# so, the base class must be abstract class in this scenario and shpould contain all the methods specifially created in each sub-classes like a template
# so, we cannot instantiate from the parent class once we defined as abstract base class

# also, we should define the spefic methods used by the sub classes as abstract method declarator, otherwise the subclass will be considered as abstract method

# inheritance

from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

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

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("reading from a file")


class NetworkStream(Stream):
    def read(self):
        print("reading from a network")


class VideoStream(Stream):
    # TypeError: Can't instantiate abstract class VideoStream without an implementation for abstract method 'read'
    pass


stream = FileStream()

video = VideoStream()
