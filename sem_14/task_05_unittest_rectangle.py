"""На семинарах по ООП был создан класс прямоугольник
хранящий длину и ширину, а также вычисляющую периметр,
площадь и позволяющий складывать и вычитать
прямоугольники беря за основу периметр.
Напишите 3-7 тестов unittest для данного класса.
"""
import unittest
from rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def setUp(self) -> None:
        self.rect1 = Rectangle(5)
        self.rect2 = Rectangle(6)

    def testMakingSquare(self):
        self.assertIsInstance(self.rect1, Rectangle, msg="Can't make a rectangle")

    def testPerimetr(self):
        self.assertEqual(self.rect1.perimeter(), 20, msg="Wrong perimetr")

    def testArea(self):
        self.assertEqual(self.rect1.area(), 25, msg="Wrong area")

    def testAddition(self):
        self.assertEqual(self.rect1 + self.rect2, Rectangle(11, 11), msg="Wrong addition")

    def testSubtraction(self):
        self.assertEqual(self.rect2 - self.rect1, Rectangle(1, 1), msg="Wrong subtraction")

    def testEqual(self):
        self.assertEqual(self.rect1 == self.rect2, False, msg="Wrong equality")

    def testNotEqual(self):
        self.assertEqual(self.rect1 != self.rect2, True, msg="Wrong equality")

    def testGreater(self):
        self.assertEqual(self.rect1 > self.rect2, False, msg="Wrong greater equality")

    def testGreaterOrEqual(self):
        self.assertEqual(self.rect1 >= self.rect2, False, msg="Wrong greater or equal equality")

    def testLess(self):
        self.assertEqual(self.rect1 < self.rect2, True, msg="Wrong less equality")

    def testLessOrEqual(self):
        self.assertEqual(self.rect1 <= self.rect2, True, msg="Wrong less or equal equality")


if __name__ == "__main__":
    unittest.main(verbosity=2)
