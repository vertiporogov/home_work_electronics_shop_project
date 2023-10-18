from src.item import Item


class MixinLen:

    def __init__(self):
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language


class Keyboard(Item, MixinLen):

    def __init__(self, name: str, price: float, quantity: int, language='EN'):
        super().__init__(name, price, quantity)
        self.__language = language

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
            return self
        elif self.__language == 'RU':
            self.__language = 'EN'
            return self
