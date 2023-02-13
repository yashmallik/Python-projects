import csv


class Thing():
    pay_discount = 0.8
    all = []

    def __init__(self, name: str, price: float):
        assert price >= 0, f"price must not be lower than zero"

        self.__name = name
        self.__price = price

        Thing.all.append(self)

    @property
    def price(self):
        return self.__price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("name should be less than character 10")
        else:
            self.__name = value

    @classmethod
    def instantiate_from_csv(cls):
        with open("oops.csv", "r") as f:
            reader = csv.DictReader(f)
            list_items = list(reader)
        for item in list_items:
            Thing(
                name=item['name'],
                price=float(item['price'])

            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.__price})"

    def discount(self):
        self.__price = self.__price*self.pay_discount

    def increament(self, increament_value):
        self.__price += self.__price*(increament_value/100)
