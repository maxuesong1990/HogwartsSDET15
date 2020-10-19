from pythoncode.calcylator import Calculator


class TestCalc:
    def test_add(self):
        calc=Calculator()
        result=calc.add(1,1)
        assert result ==2
