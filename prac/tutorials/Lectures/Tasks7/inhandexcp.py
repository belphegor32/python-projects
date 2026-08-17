class A:
    a = 100500

class B(A):
    b = 42

# print(dir(B))

class A:
    def __init__(self, val=0):
        self.val = val
    def __add__(self, other):
        return self.__class__(self.val + other.val)
    def __str__(self):
        return f"<{self.val}>"

a, b = A(2), A(3)
print(a + b)

class B(A):
    def __str__(self):
        res = super().__str__()
        return "<<" + res + ">>"

a, b = B(2), B(3)
print(a + b)

# Q = type("CCC", (), {"val": 100500, "x": 42})
# print(dir(Q))
# ASD = type("InhQ", (Q,), {"x": -1, "y": -2})
# print(dir(ASD))

class A:
    def __str__(self):
        return f"<{self.val}>"

class B:
    def __init__(self, val):
        self.val = val

class C(A, B):
    pass

print(C(1234))
c = C(100500)
print(isinstance(c, C))
print(isinstance(c, A))
print(isinstance(c, B))
print(issubclass(C, A))
print(issubclass(A, B))

class UStr(str):
    def __neg__(self):
        return self.__class__("".join(reversed(self)))

s = UStr("123")
print(-s)


class E_A(Exception):
    pass 
class E_B(E_A):
    pass
class E_C(E_B):
    pass

for ext in (E_A, E_B, E_C):
    try:
        raise ext
    except E_C:
        print("C")
    except E_B:
        print("B")
    except E_A:
        print("A")

def genex(arg):
    raise RuntimeError(arg)

try: 
    genex("100")
except Exception as E:
    print(dir(E))
    print(E)


for ext in (E_A, E_B, E_C, None):
    try:
        if ext:
            raise ext
    except E_C:
        print("C")
    except E_B:
        print("B")
    except E_A:
        print("A")
    else:
        print("No exc")
    finally:
        print("FIN")


from math import inf

def divisor(a, b):
    return a / b

def divv(a, b, div=divisor):
    try: 
        return div(a, b)
    except ZeroDivisionError:
        return inf