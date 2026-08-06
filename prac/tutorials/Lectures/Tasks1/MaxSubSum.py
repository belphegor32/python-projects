current = best = int(input())

while (x := int(input())) != 0:
    current = max(x, current + x)
    best = max(best, current)

print(best)