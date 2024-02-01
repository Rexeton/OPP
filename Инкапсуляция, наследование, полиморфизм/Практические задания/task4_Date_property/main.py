class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    def __init__(self, day: int, month: int, year: int):
        self._day = self.check_numbers(day,"День")
        self._month = self.check_numbers(month,"Месяц")
        self._year = self.check_numbers(year,"Год")

        self.is_valid_date(self._day, self._month, self._year)

    # TODO какой декоратор следует применить?
    @staticmethod
    def is_leap_year(year):
        """Проверяет, является ли год високосным"""
        is_leap=0
        if year % 4==0:
            is_leap = 1
            # TODO реализовать метод
        return is_leap  # TODO записать условие проверки високосного года

    @staticmethod
    def get_max_day(month: int, year):
        """Возвращает максимальное количество дней в месяце для указанного года"""
        return Date.DAY_OF_MONTH[Date.is_leap_year(year)][month-1] # TODO вернуть количество дней указанного месяца

    @staticmethod
    def is_valid_date(day: int, month, year):
        """Проверяет, является ли дата корректной"""
        max_day=Date.get_max_day(month,year)
        if max_day<day:
            raise ValueError(f"Такой даты не бывает. Последний день этого месяца {max_day}")
        return True  # TODO если указанный набор день, месяц и год неверны, то вызвать ошибку ValueError

    def check_numbers(self,num,name_param):
        if not isinstance(num,int):
            raise TypeError(f"{name_param} должен быть числом")
        if num<0 and name_param != "Год":
            raise ValueError(f"{name_param} отрицательным не бывает")
        if num>12 and name_param=="Месяц":
            raise ValueError(f"{name_param} не может быть {num}")
        return num

    # TODO записать getter и setter для дня
    @property
    def day(self):
        return self._day
    @day.setter
    def day(self,day):
        self._day= self.check_numbers(day,"День")
        self.is_valid_date(self._day,self._month,self._year)

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self,month):
        self._month = self.check_numbers(month,"Месяц")

    @property
    def year(self):
        return self._month

    @year.setter
    def year(self,year):
        self._year = self.check_numbers(year, "Год")
    # TODO записать getter и setter для месяца

    # TODO записать getter и setter для года
    def __str__(self):
        return f'Дата {self._day}/{self._month}/{self._year}'
if __name__=='__main__':
    date=Date(1,1,2024)
    date.day=5
    date.month=12
    date.year=2020
    print(date)