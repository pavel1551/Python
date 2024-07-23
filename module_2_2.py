# Задача "Все ли равны?":
# На вход программе подаются 3 целых числа и записываются в переменные first, second и third соответственно.
# Ваша задача написать условную конструкцию (из if, elif, else), которая выводит кол-во одинаковых чисел среди 3-х введённых.
#
# Пункты задачи:
# Если все числа равны между собой, то вывести 3
# Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 210
# Если равных чисел среди 3-х вообще нет, то вывести 0


first = int(input("Введите 1 число: "))
second = int(input("Введите 2 число: "))
third = int(input("Введите 3 число: "))

# if first % 3 == 0 and first % 5 ==0:
#     print('FizzBuzz')
#
# elif first % 3 ==0:
#     print('Fizz')
# elif first % 5 ==0:
#     print('Buzz')
# else:
#     print('Число не подходит')

if first == second and second == third and third == first:
    print(3)
elif first == second or second == third or third == first:
    print(2)
else:
    print(0)