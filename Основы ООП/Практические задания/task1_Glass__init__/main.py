from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        self.capacity_volume=self.check_volume(capacity_volume,"Объем стакана")
        self.occupied_volume=self.check_volume(occupied_volume,"Заполненный объем стакана")
        if occupied_volume>capacity_volume:
            raise ValueError("Заполненный объем стакана не может быть больше общего объема")


    def check_volume(self, capacity_volume,name_of_valume):
        if not (isinstance(capacity_volume,int) or isinstance(capacity_volume,float)):
            raise TypeError(f"{name_of_valume} должен быть типа int или float")
        if capacity_volume<0:
            raise ValueError(f"{name_of_valume} не может быть меньше 0")
        return capacity_volume



          # TODO инициализировать объект "Стакан"




if __name__ == "__main__":
    Glass_1=Glass(20,50)
    Glass_2 = Glass(10, 60)
    print(Glass_1.capacity_volume)
    print(Glass_2.occupied_volume)

    Glass_error= Glass(1,3)
      # TODO инициализировать два объекта типа Glass
    # TODO попробовать инициализировать не корректные объекты
