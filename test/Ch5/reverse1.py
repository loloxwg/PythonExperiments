def Reverse(v):
    t = v[::]
    r = []

    while t:
        tt = max(t)
        r.append(tt)
        t.remove(tt)
    return r