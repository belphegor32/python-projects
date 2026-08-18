# def fun(a, b):
#     return a + 2*b

# res = fun(1, 2)
# def dumper(f):
#     def newf(*args):
#         print(args)
#         res = f(*args)
#         print(res)
#         return res
#     return newf

# ff = dumper(fun)
# ff(3, 5)
# fun = dumper(fun)
# fun(1, 2)

# @dumper
# def mulmul(a, b):
#     return a * b


# def decor(n):
#     def dec(f):
#         def newfun(*args):
#             res = f(*args)
#             return [res] * n
#         return newfun
#     return dec

# @decor(5)
# def fun(a, b):
#     return a + b * 2
# print(fun(3, 4))


# class Timer:
#     from time import time 
#     def __init__(self, f):
#         self.fun = f
#     def __call__(self, *args):
#         start_time = self.time()
#         res = self.fun(*args)
#         diff = self.time() - start_time
#         print(f"Execution time: {diff}")
#         return res


# @Timer
# def f(a, b):
#     return sum(i + j for i in range(a) for j in range(b))
# f(1000, 1000)


# class C:
#     def __str__(self):
#         return "@@@"

# def braced(cls):
#     cls.__str = cls.__str__
#     cls.__str__ = lambda s: "<<" + cls.__str() + ">>"
#     return cls

# print(str(C()))

# @braced 
# class C:
#     def __str__(self):
#         return "@@@"

# def braced(cls):
#     class newcls(cls):
#         def __str__(self):
#             return "<<" + super().__str__() + ">>"
#     return newcls

# @braced
# class C(int):
#     pass

# c = C(123)
# print(c)
# print(c + 1)

# from random import random
# class Descr:
#     def __get__(self, obj, cls):
#         return int.__add__ if random() > 0.4 else int.__sub__

# class A:
#     sumadd = Descr()

# a = A()
# print(a.sumadd)

class Descr:
    def __get__(self, obj, cls):
        print("Get from", obj)
        return obj._value

    def __set__(self, obj, val):
        print(f"Set {val} to", obj)
        obj._value = val

    def __delete__(self, obj):
        print("Do not delete")


class A:
    field = Descr()
    def __init__(self):
        self.field = 0

a = A()

a.field = 100500
print(a.field)
del a.field


class Descr:
    def __get__(self, obj, cls):
        return obj.__dict__[self.key]
    def __set__(self, obj, val):
        obj.__dict__[self.key] = abs(val)
    def __set_name__(self, owner, name):
        self.key = name

class C:
    d = Descr()
    e = Descr()

c = C()
c.d = 100
c.e = 100
c.e = 200
print(c.e, c.d)


class C:
    __slots__ = "a", "b", "c"
    ro = "read only"
    def __init__(self, x, y, z):
        self.a, self.b, self.c = x, y, z

c = C(12, 23, 34)
print(c.a)


# манипуляция с первым параметром метода
class C:
    def fun(*args):
        print("Normal:", args)

    @classmethod
    def cfun(*args):
        print("Class method", args)

    @staticmethod
    def sfun(*args):
        print("Static method", args)

