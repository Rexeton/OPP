class Calculator:
    # TODO написать статические методы
    @staticmethod
    def add (a, b):  # TODO сделать статическим методом
        """ Формула площади по двум сторонам и углу между ними. """
        return a + b
    @staticmethod
    def mul (a, b):  # TODO сделать статическим методом
        """ Формула площади по двум сторонам и углу между ними. """
        return a * b
if __name__ == "__main__":
    print(Calculator.add(5, 6))  # 11
    print(Calculator.mul(5, 6))  # 30
