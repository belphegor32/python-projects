def products(n, start = 2, prefix = ()): 
    d = start

    while d * d <= n:
        if n % d == 0:
            products(n // d, d, prefix + (d,))

        d += 1

    print("*".join(map(str, prefix + (n,))))


n = int(input())
products(n)