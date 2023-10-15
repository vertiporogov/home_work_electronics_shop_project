from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, new_number_of_sim):
        if new_number_of_sim is not int and new_number_of_sim < 1:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля')

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        return f"{self.name}"

    # def __add__(self, other):
    #     if isinstance(other, self.__class__):
    #         return self.quantity + other.quantity
    #     return None
