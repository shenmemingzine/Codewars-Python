def array_diff(a, b):
    if a != []:
        new = []
        for e in a:
            if e not in b:
                new.append(e)
        return new
    return []
