"""
Цель: Написать программу на языке Python с использованием Pycharm для работы с методами строк и организации программ.

1. В проекте, где вы решаете домашние задания, создайте модуль 'homework4.py' и напишите весь код в нём.

2. Организуйте программу:
Создайте переменную my_string и присвойте ей значение строки с произвольным текстом (функция input()).
Вывести количество символов введённого текста
3. Работа с методами строк:
Используя методы строк, выполните следующие действия:
Выведите строку my_string в верхнем регистре.
Выведите строку my_string в нижнем регистре.
Измените строку my_string, удалив все пробелы.
Выведите первый символ строки my_string.
Выведите последний символ строки my_string.

Примечания:
Для вывода значений на экран используйте функцию print().
Для вызова методов строк используйте операцию точки '.'.
"""

my_string = input()
print(len(my_string)) #Вывод кол-ва символов введённого текста - используем метод len()

print(my_string.upper()) # .upper() - верхний регистр
print(my_string.lower()) # .lower() - нижний регистр

print(my_string.replace(' ','')) #Замена символов .replace - в данном случае удаляем пробел

print(my_string[-1])