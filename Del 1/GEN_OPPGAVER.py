import timeit

def funk1():
    tall = 14
    if tall == 0:
        return 1
    elif tall == 6:
        return 2
    elif tall == 13:
        return 56
    elif tall == 81:
        return 13
    elif tall >= 90:
        return 0
    elif tall < -4:
        return 3
    elif tall == 44 or 74:
        return 77
    else:
        return 5

def funk2():
    tall = 14
    match tall:
        case 0: return 1
        case 6: return 2
        case 13: return 56
        case 81: return 13
        case 90: return 0
        case tall if tall < -4: return 3
        case 44 | 74: return 77
        case _: return 5

print(f"{timeit.timeit(funk1, number=10000)}s for å kjøre funk1 10000 ganger")
print(f"{timeit.timeit(funk2, number=10000)}s for å kjøre funk2 10000 ganger")