first = int(input('ВВедите вервое число: '))
print('Введённое число: ',first)
second = int(input('ВВедите второе число: '))
print('Введённое число: ',second)
third = int(input('ВВедите третье число: '))
print('Введённое число: ',third)

if first==second and second==third and first==third:
    print('3')
elif first==second or second==third or first==third:
    print('2')
else :
    print('0')