class ISUB:
    def __init_subclass__(cls, **kwargs):
        print(kwargs, cls)
        super().__init_subclass__()


class C(ISUB, parameter="QQ"):
    pass

print(type(type))
type("C", (), {"A": 123})
print(C)

C = type("Simple", (), {"val": 42, "getval": lambda self: self.val})

class overtype(type):
    def __init__(self, *args, **kwargs):
        print(args, kwargs)
        super().__init__(*args, **kwargs)

C = overtype("C", (), {"A": 123})
print(C)

class C(metaclass=overtype):
    A = 100500

print(C)


class Final(type):
    def __new__(metacls, name, parents, namespace):
        for parent in parents:
            if isinstance(parent, Final):
                raise TypeError(f"No inheritance from {parent}")

        return super().__new__(metacls, name, parents, namespace)


class E(metaclass=Final):
    a = 1

class Singleton(type):
    _instance = None
    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class C(metaclass=Singleton):
    A = 100500

c = C()
d = C()
print(c is d)

cmd = "help command"
cmd.split()
if cmd.split() == ["help"]:
    print("help")
elif cmd.split() == ["help", "command"]:
    print("help of command")

cmd = "help go go go"
match cmd.split():
    case ["help" | "usage" as topic]:
        print(f"Help = {topic}")
    case ["help", "command"]:
        print("help of command")
    case ["help", command]:
        print(f"Help on {command}")
    case ["help", *cmd_w_args] if len(cmd_w_args) < 3:
        print(f"help on", *cmd_w_args)
    case _:
        print("UNKNOWN")


match v := eval(input()):
    case int(n):
        print(f"Integer {n}")
    case float():
        print(f"Float {v}")

print(v == n)


d = {1:2, 3:4, 5:6}
match d:
    case {3:4}:
        print("3, 4")

match d:
    case var:
        print(var)

var = {1:3}

import inspect

class C:
    A: int 
    B: float = 1.2
    def __init__(self, a: int, b: float):
        self.A, self.B = a, b
    def sum(self) -> float:
        return self.A + self.B

print(inspect.get_annotations(C))