# f = lambda a, b: a * 2 + b

# wprint(f(23, 54))

# lst = list(range(1, 20))

# print(sorted(lst, key=lambda el: el % 3))

# def fun(a, *b):
#    print(a, b)

# fun(1, 2, 3, 5)

# def fun(a, b=1, /, c="QQ", *, d="55"):
#     print(a, b, c, d)

# def fun(a, b):
#     """Returns a formula over a, b"""
#     return a*2 + b

# print(fun.__doc__)
# # help(fun)

# closures
def FUN(c):
    def fun(x):
        return x + c
    return fun 

f = FUN(100500)
print(f(123))