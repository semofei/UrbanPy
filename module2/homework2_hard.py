n = 0
state = False
def n_input():      #с помощью этой функции я объявляю первое число
    n = int(input('введи число от 3 до 20 включительно:'))
    return n

n = n_input()
while state == False:   #этот цикл проверяет введённое число на соответствие уловиям введённого числа: от 3 до 20
    if n < 3 or n > 20:
        print('введено неверное число')
        n = n_input()
    else:
        state = True

less_nums = []
count = 1
while count < n:        #здесь я составляю список из всех чисел, которые меньше данного
    less_nums.append(count)
    count += 1

pairs = []
for i in less_nums:     #здесь я составляю комбинации из всех чисел
    j = i-1             #чтобы числа в парах не повторялись нужно заменить на j = i
    while j < len(less_nums):
        pairs.append([less_nums[i-1],less_nums[j]])
        j+=1
        if sum(pairs[-1]) > n:  #если сумма пары чисел превышает заданное число n, то такая пара и последующие j-е пары выбывают
            pairs.pop()
            break
print(type(pairs[1]))

result = []
for pair in pairs:      #проверка на кратность
    if n % sum(pair) == 0:
        result.append(pair)


print('result:', *result, sep=' | ')

# print(count)
# print(less_nums)
# print(pairs)

# Задание "Слишком древний шифр":
# Вы отправились в путешествие на необитаемый остров и конечно же в очередной вылазке в джунгли вы попали в ловушку местному племени (да-да, классика "Индиана Джонса").
# К вашему удивлению, в племени были неплохие математики и по совместительству фантазёры.
# Вы поняли это, когда после долгих блужданий перед вами появились ворота (выход из ловушки) с двумя каменными вставками для чисел.
# В первом поле камни с числом менялись постоянно (от 3 до 20) случайным образом, а второе было всегда пустым.
#
# К вашему счастью рядом с менее успешными и уже неговорящими путешественниками находился папирус, где были написаны правила для решения этого "ребуса". (Как жаль, что они поняли это так поздно :( ).
#
# Во вторую вставку нужно было написать те пары чисел друг за другом, чтобы число из первой вставки было кратно(делилось без остатка) сумме их значений.