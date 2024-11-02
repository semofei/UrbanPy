def apply_all_func(int_list: list, *functions):
    if not int or float in int_list:
        raise TypeError
    results = dict()
    for func in functions:
        temp = func(int_list)
        results[func.__name__] = temp
    return results


print(apply_all_func([6, 20.0, 15, 9.6], max, min))
print(apply_all_func([6, 20, 1.5, 9], len, sum, sorted))
