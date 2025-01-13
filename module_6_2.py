class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner  # владелец транспорта
        self.__model__ = model  # модель транспорта
        self.__engine_power__ = engine_power  # мощность двигателя
        self.__color__ = color  # цвет транспорта

    def get_model(self):
        return f"Модель: {self.__model__}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power__}"

    def get_color(self):
        return f"Цвет: {self.__color__}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color):
        # Проверяем доступность нового цвета
        if new_color.lower() in [color.lower() for color in self.__COLOR_VARIANTS]:
            self.__color__ = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner, model, color, engine_power):
        super().__init__(owner, model, color, engine_power)


# Тестируем работу классов
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства
vehicle1.set_color('Pink')  # Недопустимый цвет
vehicle1.set_color('BLACK')  # Допустимый цвет
vehicle1.owner = 'Vasyok'  # Меняем владельца

# Проверяем изменения
vehicle1.print_info()