def pattsort(pattern, seq):
    p = sorted(pattern)
    s = sorted(seq)

    match = dict(zip(p, s))

    return [match[x] for x in pattern]


