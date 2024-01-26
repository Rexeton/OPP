class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    def __init__(self, day: int, month: int, year: int):
        self.day = self.check_numbers(day)
        self.month = self.check_numbers(month)
        self.year = self.check_numbers(year)

        self.is_valid_date(self.day, self.month, self.year)
    @staticmethod
    def is_leap_year(year: int):
        """Проверяет, является ли год високосным"""
        is_leap=0
        if year % 4==0:
            is_leap = 1
            # TODO реализовать метод
        return is_leap
    def get_max_day(self,month: int, year: int):
        """Возвращает максимальное количество дней в месяце для указанного года"""
        return self.DAY_OF_MONTH[self.is_leap_year(year)][month+1] # TODO используя атрибут класса DAY_OF_MONTH вернуть количество дней в запрашиваемом месяце и году

    def is_valid_date(self,day: int, month: int, year: int):
        """Проверяет, является ли дата корректной"""
        if self.get_max_day(month,year)<day:
            return False
        return True  # TODO проверить валидность даты
    def check_numbers(self,num):
        if not isinstance(num,int):
            raise TypeError("В дате должны быть числа")
        if num<0:
            raise ValueError("Отрицательных чисел не должно быть")

Date1=Date(30,3,2024)
