# def subr(n):
#     yield f"One/{n}"
#     yield f"Two/{n}"
#     return f"Done {n}"

# def task():
#     for i in range(3):
#         result = yield from subr(i)
#         yield result
#     return "All done"

# core = task()
# try:
#     while (res := next(core)):
#         print(res)
# except StopIteration as e:
#     print(e.value)


# def task(init):
#     val = init
#     while True:
#         val = yield f"<{val}>"


# core = task(100500)
# res = next(core)
# print(f"Start: {res}")
# for i in range(5):
#     res = core.send(i)
#     print(res)


# def subt():
#     x = yield "want x"
#     y = yield f"{x=}, want y"
#     return x, y

# def task():
#     while True:
#         value = yield from subt()
#         _ = yield value


# core = task()
# print(core.send(None))
# for i in range(9):
#     print(core.send(i))


# def subt(n):
#     x = yield f"Subtask {n} want x"
#     y = yield f"Subtask {n} want y"
#     return x, y

# def task(n):
#     while True:
#         value = yield from subt(n)
#         _ = yield f"Task {n}: {value}"


# cores = task(0), task(1)
# print(cores[0].send(None), cores[1].send(None))

# for i in range(12):
#     print(cores[i%3 == 0].send(i))


# async def hello(name):
#     print(f"Hello!, {name}")
#     return 42

# async def hello2(name):
#     res = await hello(name)
#     res2 = await hello(name)
#     print(">>", res, res2)
    
# hello2("you").send(None)


