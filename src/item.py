# from _pytest.nodes import Item
import csv


# list_devices = []
# with open('src/items.csv', encoding='utf-8') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         list_devices.append(row)
class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.new_name = str
        Item.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = int(self.price * self.pay_rate)

    @property
    def get_name(self):
        return self.__name

    @get_name.setter
    def get_name(self, name):
        self.__name = name
        if len(name) > 10:
            return name[:9]
        return name

    @classmethod
    def instantiate_from_csv(cls):
        # hh = 'src/items.csv'
        with open('items.csv', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                cls.name = row['name']
                cls.price = row['price']
                cls.quantity = row['quantity']
                Item.all.append(cls)

        return Item.all

    @staticmethod
    def string_to_number(data_string):
        return int(data_string)


# print(Item.instantiate_from_csv())