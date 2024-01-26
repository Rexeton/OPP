class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    def __init__(self, day: int, month: int, year: int):

        self.day = self.check_numbers(day,"День")
        self.month = self.check_numbers(month,"Месяц")
        self.year = self.check_numbers(year,"Год")
        self.is_valid_date(day, month, year)



    @staticmethod
    def is_leap_year(year):
        """Проверяет, является ли год високосным"""
        is_leap=0
        if year % 4==0:
            is_leap = 1
            # TODO реализовать метод
        return is_leap

    @staticmethod
    def get_max_day(month: int, year):
        """Возвращает максимальное количество дней в месяце для указанного года"""
        return Date.DAY_OF_MONTH[Date.is_leap_year(year)][month-1] # TODO используя атрибут класса DAY_OF_MONTH вернуть количество дней в запрашиваемом месяце и году

    @staticmethod
    def is_valid_date(day: int, month, year):
        """Проверяет, является ли дата корректной"""
        max_day=Date.get_max_day(month,year)
        if max_day<day:
            raise ValueError(f"Такой даты не бывает. Последний день этого месяца {max_day}")
        return True  # TODO проверить валидность даты
    def check_numbers(self,num,name_param):
        if not isinstance(num,int):
            raise TypeError(f"{name_param} должен быть числом")
        if num<0 and name_param != "Год":
            raise ValueError(f"{name_param} отрицательным не бывает")
        if num>12 and name_param=="Месяц":
            raise ValueError(f"{name_param} не может быть {num}")


Date1=Date(29,2,2023)
