class Fraction:

    def __init__(self, integer_value) -> None:
        super().__init__()
        self.integer_value = integer_value

    def plus(self, param):
        return self

    def int_value(self):
        return self.integer_value


def test_zero_plus_zero():
    sum = Fraction(0).plus(Fraction(0))
    assert sum.int_value() == 0


def test_non_zero_plus_zero():
    sum = Fraction(3).plus(Fraction(0))
    assert sum.int_value() == 3


"""
0 + 0 = 0
3 + 0 = 0
0 + 5 = 0
3 + 4 = 7

-3 + 1 = -2

1/5 + 2/5 = 3/5

1/2 + 1/3 = 5/6

3/4 + 5/8 = 11/8

1/6 + 4/9 = 11/18

-1/4 + 3/4 = 1/2
3/8 + -1/2 = -1/8

1/-4 + (-3/-4)  = 1/2
"""
