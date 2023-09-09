from fibonacci_sequence import fib 
from random import randint

n = randint(15, 35)
fibvalue, excTime = fib(n)
print('fib(', n,') ', fibvalue, end = '\n')
print('fib(', n,') took ', excTime, 'seconds')
