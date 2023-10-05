import csv


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
        self.__name = name[:10]
        self.price = price
        self.quantity = quantity
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
    def name(self):
        name = self.__name
        return name

    @name.setter
    def name(self, new_name):
        self.__name = new_name[:10]

    @classmethod
    def instantiate_from_csv(cls):
        """ Класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv """
        cls.all.clear()
        with open('../src/items.csv', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                cls(row['name'], float(row['price']), int(row['quantity']))

    @staticmethod
    def string_to_number(data_string):
        """Метод для изменения str на int"""

        return int(float(data_string))
