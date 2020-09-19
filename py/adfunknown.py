from abc import ABCMeta, abstractmethod
import numpy as np

class ADFunknown(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def initunknown(self):
        pass

    @abstractmethod
    def input(self):
        pass

    @abstractmethod
    def output(self, input):
        pass