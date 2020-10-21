import pytest

from pythoncode.calcylator import Calculator


class TestCalc_1015:
    def setup(self):
        print("【计算开始】")
        self.calc = Calculator()

    def teardown(self):
        print("计算结束】")

    @pytest.mark.parametrize('a,b,c', [[1, 1, 2], [1, 2, 4], [(1), 4, [6]], ['a', 'b', 'c'],
                                       [100000000000000, 100000000000000, 200000000000000]])
    def test_add(self, a, b, c):
        try:
            if (self.calc.add(a, b) == c):
                print(self.calc.add(a, b))
                print("计算正确")
            elif (self.calc.add(a, b) != c):
                print("计算出错")
        except AssertionError as e:
                print("输入不合法")

    @pytest.mark.parametrize('a,b,c', [[1, 1, 1], [4, 2, 1], [2, 0, 1],[2.0, 2, 1.0],['a', 'b', 'c'],[(1), 4, [6]]])
    def test_div(self, a, b, c):
        if b == 0:
            print("除数不能为0")
        else:
            try:
                if (self.calc.div(a, b) == c):
                    print(self.calc.div(a, b))
                    print("计算正确")
                elif (self.calc.div(a, b) != c):
                    print("计算出错")
            except TypeError as e:
                print("输入不合法")




