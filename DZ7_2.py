from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.__param = param

    def get_param(self):
        return self.__param

    @abstractmethod
    def common_charge(self):
        pass


class Coat(Clothes):
    @property
    def common_charge(self):
        return self.get_param() / 6.5 + 0.5


class Suit(Clothes):
    @property
    def common_charge(self):
        return self.get_param() * 2 + 0.3


coat1 = Coat(52)
print(coat1.common_charge)
suit1 = Suit(5)
print(suit1.common_charge)