# from modules import *

# class Coffee():
#     def cost(self):
#         return 2

# def cache(func):
#     # Keep a dict of values returned already
#     vals = {}

#     def wrapper(x):
#         if not vals.has_key(x):
#             vals[x] = func(x)
#         return vals[x]

#     wrapper.__doc__ = func.__doc__

#     return wrapper

# @cache
# def fib(x):
#     """Fibonacci series

#     >>> fib(1)
#     1
#     >>> fib(2)
#     2

#     """
#     if x < 0:
#         raise ValueError('Must be greater than 0')
#     elif x == 0:
#         return 1
#     elif x == 1:
#         return 1
#     else:
#         return fib(x - 1) + fib(x - 2)