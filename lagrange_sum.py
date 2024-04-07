from random import shuffle
from math import isqrt

x = int(input('Write a natural number for the Lagrange Sum: '))

def lagrange_sum(p):
        num = a = b = c = d = 0           
        if num<p:
            a = int(isqrt(abs(p - b**2 - c**2 - d**2)))
            b = int(isqrt(abs(p - a**2 - c**2 - d**2)))
            c = int(isqrt(abs(p - a**2 - b**2 - d**2)))
            d = int(isqrt(abs(p - a**2 - b**2 - c**2)))
            p = []

            squared_values = [a, b, c, d]
            p.extend(squared_values)
            sum_evaluation = x == a**2 + b**2 + c**2 + d**2
            
            if sum_evaluation:
                print(p)
            else:
                shuffle(squared_values)
                print(squared_values)

if __name__ == '__main__':
    lagrange_sum(x)



