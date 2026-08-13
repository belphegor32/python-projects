seq = iter("ABCD")
print(seq)
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
# print(next(seq)) StopIteration
print(list(seq))


def pred(i):
    return -1 < i < 2

seq2 = filter(pred, (12, 54, -4, 1, 2, 0, 4, 7))
print(list(seq2))

class C:
    def __getitem__(self, idx):
        return f"<{idx}>"

c = C()
e = iter(c)
print(next(e))
print(next(e))


for i in "ABCD":
    print(i, type(i))

g = (i % 3 for i in range(10))
print(type(g))
print(next(g))

print(sorted((i % 3 for i in range(10)), key=lambda x: x % 2))

def genf(n):
    yield "START"
    for i in range(n):
        yield f"<{i}>"
    yield "END"

e = genf(5)
print(list(e))

def find13(seq):
    for el in seq:
        if el == 13:
            return 
        else:
            res = el * 2
            yield res

e = find13(range(10, 20))
next(e)
print(e.gi_frame.f_locals)


def gen(seq):
    for el in seq:
        yield f"<{el}>"

list(gen("ABC"))

def repeat(seq, n):
    for i in range(n):
        yield from gen(seq)

print(list(repeat(gen("DEF"), 3)))