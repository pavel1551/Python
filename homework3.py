"""
  - Создайте переменную name и присвойте ей значение вашего имени (строка).
  - Выведите значение переменной name на экран.
  - Создайте переменную age и присвойте ей значение вашего возраста (целое число).
  - Выведите значение переменной age на экран.
  - Перезапишите в age текущее значение переменной age + новое.
Как неверно (просто перезапись на новое число):
a = 15
a = 17
  - Выведите измененное значение переменной age на экран.
  - Создайте переменную is_student и присвойте ей значение True (логическое значение).
  - Выведите значение переменной is_student на экран.
"""

name = 'Pavel'
print(name, type(name))
age = 21
print(age, type(age))
age = age + 1 #Если прибавить не целое число, то получится тип данных float
print(age, type(age)) #Проверка типа данных
is_student = True
print(is_student, type(is_student))