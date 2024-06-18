"""sample test"""

from django.test import SimpleTestCase

from . import calc


class calctest(SimpleTestCase):
    """tests the calc module """

    def test_add_numbers(self):
        res = calc.add(5, 6)
        self.assertEquals(res, 11)

    def test_sub_numbers(self):
        res = calc.sub(10, 15)
        self.assertEquals(res, 5)
