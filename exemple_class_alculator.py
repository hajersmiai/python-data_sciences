class Calculator:
    def __init__(self, initial_value =0):
        self.result=initial_value
    def add(self, amount):
        self.result +=amount
        return self.result
calc = Calculator(20)
print (calc.result)
calc.add(5)
print (calc.result)

