class Descript:

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def get(self, instance, owner):
        return getattr(instance, self.param_name)

    def set(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if value > 0:
            self.side = value
        else:
            raise ValueError(
                'Значение длины стороны не должно быть отрицательным')


class Rectangle:
    """Класс Прямоугольник.
    Доработан - добавлен метод сложения и вычитания по перметрам
    Добавлены методы сравнения прямоугльников по площади"""

    # slots = ("side_1", "side_2")  # доработка без словаря dict

    side_1 = Descript()
    side_2 = Descript()

    def __init__(self, side_1, side_2=0) -> None:
        self.side_1 = side_1
        if side_2 == 0:
            self.side_2 = side_1
        else:
            self.side_2 = side_2

    def perimeter_rectangle(self):
        return (self.side_1 + self.side_2) * 2

    def area_rectangle(self):
        return self.side_1 * self.side_2

    def add(self, other):
        common_p = self.perimeter_rectangle() + other.perimeter_rectangle()
        newside_1 = max(self.side_1, self.side_2,
                        other.side_1, other.side_2)
        newside_2 = int((common_p - 2 * newside_1) / 2)
        print(newside_1, newside_2)
        return Rectangle(newside_1, newside_2)

    def sub(self, other):
        difference = abs(self.perimeter_rectangle() -
                         other.perimeter_rectangle())
        newside_1 = min(self.side_1, self.side_2,
                        other.side_1, other.side_2)
        newside_2 = int((difference - 2 * newside_1) / 2)
        if newside_2 < 0:
            newside_1 = newside_2 = difference / 4
        print(newside_1, newside_2)
        return Rectangle(newside_1, newside_2)

    def eq(self, other) -> bool:  # равно ==
        if self.area_rectangle() == other.area_rectangle():
            return True
        return False

    def ne(self, other) -> bool:  # не равно !=
        if self.area_rectangle() != other.area_rectangle():
            return True
        return False

    def gt(self, other) -> bool:  # больше, >
        if self.area_rectangle() > other.area_rectangle():
            return True
        return False

    def ge(self, other) -> bool:  # не больше, меньше или равно, <=
        if self.area_rectangle() <= other.area_rectangle():
            return True
        return False

    def lt(self, other) -> bool:  # меньше, <
        if self.area_rectangle() < other.area_rectangle():
            return True
        return False

    def le(self, other) -> bool:  # не меньше, больше или равно, >=
        if self.area_rectangle() >= other.area_rectangle():
            return True
        return False


if __name__ == "__main__":
    rect = Rectangle(5, 16)
    print(rect.area_rectangle())
    rect.side_1 = -8
    rect.side_2 = 2
    print(f'{rect.side_2=}')
    print(rect.area_rectangle())