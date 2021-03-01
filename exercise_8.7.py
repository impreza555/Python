class ComplexNumber:

    def __str__(self):
        return f'Комплексное число {self.comp_number}'

    def __init__(self, comp_number):
        self.comp_number = comp_number

    def __add__(self, other):
        return ComplexNumber(self.comp_number + other.comp_number)

    def __mul__(self, other):
        return ComplexNumber(self.comp_number * other.comp_number)


com_number1 = ComplexNumber(3 + 2j)
com_number2 = ComplexNumber(5 - 4j)
print(com_number1)
print(com_number2)
print(com_number1 + com_number2)
print(com_number1 * com_number2)
