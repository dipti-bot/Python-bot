from math import gcd

class Fraction:

    def __init__(self,x,y):
        self.num = x
        self.den = y

    def simplify(self):
        common = gcd(self.num, self.den)
        self.num //= common
        self.den //= common


    def __str__(self):
        return 'Fraction : {}/{}'.format(self.num,self.den)

    def __add__(self,other):
        new_num = self.num * other.den + self.den * other.num
        new_den = self.num * other.den 
        result = Fraction(new_num, new_den)
        result.simplify()
        return result

    def __sub__(self,other):
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den
        result = Fraction(new_num, new_den)
        result.simplify()
        return result

    def __mul__(self,other):
        new_num = self.num *  other.num 
        new_den = self.den * other.den
        result = Fraction(new_num, new_den)
        result.simplify()
        return result
    def __truediv__(self,other):
        new_num = self.num * other.den 
        new_den = self.den * other.num
        result = Fraction(new_num, new_den)
        result.simplify()
        return result

obj1 = Fraction(1,2)
obj2 = Fraction(1,2)
print(obj1)
print(obj1 + obj2)
print(obj1 - obj2)
print(obj1 * obj2)
print(obj1 / obj2)