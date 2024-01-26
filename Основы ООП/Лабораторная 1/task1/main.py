from typing import Union
# TODO Написать 3 класса с документацией и аннотацией типов

class Field:
    def __init__(self,name: str,number_of_pads: Union[int, float]):
        # Класс месторождений нефти и газа
        #number_of_pads: количество кустов на меторождении
        self.name=name
        self.number_of_pads=self.check_numbers(number_of_pads,"Кол-во кустов")

    def check_numbers(self,param,param_name):
        if not(isinstance(param,int) or isinstance(param,float)):
            raise TypeError(f"{param_name} должно быть числовым")
        if param<0:
            raise ValueError(f"{param_name} должно быть больше или равно 0")
        return param


class Pad:
    def __init__(self, name: str, number_of_wells: Union[int, float]):
        # Класс куста на месторождении нефти и газа
        # number_of_wells: количество скважин на кусту
        self.name = name
        self.number_of_wells = self.check_numbers(number_of_wells, "Кол-во скважин")
    def check_numbers(self, param, param_name):
        if not (isinstance(param, int) or isinstance(param, float)):
            raise TypeError(f"{param_name} должно быть числовым")
        if param < 0:
            raise ValueError(f"{param_name} должно быть больше или равно 0")
        return param
class Well:
    def __init__(self, name: str, Production: Union[int, float]):
        # Класс скважины на месторождении нефти и газа
        # Production: Дебит нефти
        self.name = name
        self.Production = self.check_numbers(Production, "Дебит")
    def check_numbers(self, param, param_name):

        if not (isinstance(param, int) or isinstance(param, float)):
            raise TypeError(f"{param_name} должно быть числовым")
        if param < 0:
            raise ValueError(f"{param_name} должно быть больше или равно 0")
        return param

if __name__ == "__main__":

    # TODO работоспособность экземпляров класса проверить с помощью doctest
    import doctest
    doctest.testmod()
    pass
