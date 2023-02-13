from oops_Thing import Thing


class Phone(Thing):
    def __init__(self, name: str, price: float, brokenPhone=0):
        super().__init__(
            name, price
        )
        assert brokenPhone >= 0, f"Broken phone {brokenPhone} is less than zero"

        self.brokenPhone = brokenPhone

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.brokenPhone})"
