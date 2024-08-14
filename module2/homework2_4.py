#Цель: закрепить навык решения задач при помощи цикла for,
# применив знания об основных типах данных.
# Задача "Всё не так уж просто":
#Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#Используя этот список составьте второй список primes
# содержащий только простые числа.
#А так же третий список not_primes, содержащий все не простые числа.
#Выв#едите списки primes и not_primes на экран(в консоль).

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
is_prime = True
primes =[]
not_primes = []
for num_ in numbers:
    if num_ == 1:
        print('1 not fish not meat')
        continue

    for div_ in range(2,num_):
        if num_ % div_ == 0:
#            leftover= num_%div_
            is_prime = False
            break
        else:
            is_prime = True


    if is_prime == True:
        primes.append(num_)
    else:
        not_primes.append(num_)

print(f'Primes: {primes}')
print(f'Not primes: {not_primes}')