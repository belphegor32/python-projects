def ADD (f, g): 
    def h (x): 
        return (f(x) if callable(f) else f) + (g(x) if callable(g) else g)
    return h


def SUB (f, g):
    def h (x): 
        return (f(x) if callable(f) else f) - (g(x) if callable(g) else g)
    return h


def MUL (f, g):
    def h (x): 
        return (f(x) if callable(f) else f) * (g(x) if callable(g) else g)
    return h


def MUL (f, g):
    def h (x): 
        return (f(x) if callable(f) else f) / (g(x) if callable(g) else g)
    return h