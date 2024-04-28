class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def set_numerator(self, numerator):
        self.numerator = numerator

    def set_denominator(self, denominator):
        self.denominator = denominator

    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator

    def input_data(self):
        self.numerator = int(input("Enter numerator: "))
        self.denominator = int(input("Enter denominator: "))

    def output_data(self):
        print(f"{self.numerator}/{self.denominator}")

    def add(self, other):
        result_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        result_denominator = self.denominator * other.denominator
        return Fraction(result_numerator, result_denominator)

    def subtract(self, other):
        result_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        result_denominator = self.denominator * other.denominator
        return Fraction(result_numerator, result_denominator)

    def multiply(self, other):
        result_numerator = self.numerator * other.numerator
        result_denominator = self.denominator * other.denominator
        return Fraction(result_numerator, result_denominator)

    def divide(self, other):
        result_numerator = self.numerator * other.denominator
        result_denominator = self.denominator * other.numerator
        return Fraction(result_numerator, result_denominator)


fraction1 = Fraction(1, 2)
fraction2 = Fraction(3, 4)
fraction1.output_data()
fraction2.output_data()
result = fraction1.add(fraction2)
result.output_data()
