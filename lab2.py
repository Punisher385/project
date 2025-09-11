# Батьківський клас з ЛР1
class Transport:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def info(self):
        return f"{self.brand} {self.model}, {self.year}"


# Дочірній клас з ЛР2
class Car(Transport):
    def __init__(self, brand, model, year, engine, color, mileage):
        super().__init__(brand, model, year)
        self.engine = engine
        self.color = color
        self.mileage = mileage

    # Публічний метод
    def full_info(self):
        return (f"{self.info()}, Двигун: {self.engine}, Колір: {self.color}, "
                f"Пробіг: {self.mileage} км")

    # Протектед метод (_назва)
    def _is_old(self):

        return 2025 - self.year > 10

    # Приватний метод (__назва)
    def __engine_condition(self):

        if self.mileage < 100000:
            return "Добрий стан"
        elif self.mileage < 200000:
            return "Задовільний стан"
        else:
            return "Потребує капремонту"

    # Метод, який використовує приватний
    def check_car(self):
        return f"Стан двигуна: {self.__engine_condition()}, Старий авто? {self._is_old()}"

my_car = Car("Toyota", "Camry", 2010, "2.4 бензин", "Чорний", 180000)

print(my_car.full_info())
print(my_car.check_car())
