# class D:
#     x = 0
#     def append(self, num):
#         self.x += num

# d = D()
# print(d.x)
# d.append(100)
# print(d.x)


class Num:
    num = 0
    def add(self, el):
        self.num += el
    def __str__(self):
        return f"<{self.num}>"

n = Num()
print(n)

# class D:
#     """Docs for D"""
#     def __init__(self, val):
#         """Docs for init"""
#         self.num = val
#     def __str__(self):
#         return f"<{self.num}>"

# d = D(100500)
# print(d)
# help(D)

# class D:
#     count = 0
#     def __getattr__(self, attr):
#         self.count += 1
#         return self.count

# d = D()
# d.a = 1
# d.b = 2
# d.c = 3
    

class D:
    count = 0
    def __getattribute__(self, attr):
        c = object.__getattribute__(self, "count") + 1
        object.__setattr__(self, "count", c )
        return self.count

d = D()
d.a = 1
d.b = 2
d.c = 3

class F: 
    def __del__(self):
        print(self)

c, d, e = F(), F(), F()
del d


class C:
    def __len__(self):
        return 42

print(len(C()))

class C:
    val = 0
    def __init__(self, val):
        self.val = val
    def __iter__(self):
        return iter("abc")
    def __bool__(self):
        return not self.val % 3

print(list(C(5)))


class C:
    def __init__(self, val):
        self.val = val
    def __call__(self, n):
        return f"<{self.val}>" * n

c = C("WER")
c(3)