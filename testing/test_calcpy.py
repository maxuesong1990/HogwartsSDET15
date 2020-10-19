from pythoncode.calcylator import Calculator


class TestCalc:
    def setup_class(self):
        print('计算开始')
        self.calc = Calculator()

    def teardown_class(self):
        print('计算结束')

    @pytest.mark.parametrize
    def test_add(self):
        #calc = Calculator()
        result = self.calc.add(1, 1)
        assert result == 2

    def test_add1(self):
        #calc = Calculator()
        result = self.calc.add(100, 100)
        assert result == 200

    def test_add2(self):
        #calc = Calculator()
        result = self.calc.add(0.1, 1)
        assert result == 1.1
