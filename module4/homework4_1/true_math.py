def divide(first, second):
    from math import inf
    if first == 0 and second == 0:
        return 1
    elif second == 0:
        return inf
    else:
        return first/second
