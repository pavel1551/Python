# name = input('Введите Ваше имя: ')
#
# if name == 'Павел':
#     print("Привет, администратор ", name)
# elif name != '':
#     print("Привет,", name)
# else:
#     print("Error")

number = int(input("Введите число: "))
#or - не строгий оператор (или то или то)
#and - строгий оператор (и то и  то)

if number % 3 == 0 and number % 5 ==0:
    print('FizzBuzz')

elif number % 3 ==0:
    print('Fizz')
elif number % 5 ==0:
    print('Buzz')
else:
    print('Число не подходит')

