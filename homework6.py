"""Цель: Написать программу на языке Python, используя Pycharm, для работы со словарями и множествами.

1. В проекте, где вы решаете домашние задания, создайте модуль 'homework6.py' и напишите весь код в нём.

2. Работа со словарями:
  - Создайте переменную my_dict и присвойте ей словарь из нескольких пар ключ-значение.
Например: Имя(str)-Год рождения(int).
  - Выведите на экран словарь my_dict.
  - Выведите на экран одно значение по существующему ключу, одно по отсутствующему из словаря my_dict без ошибки.
  - Добавьте ещё две произвольные пары того же формата в словарь my_dict.
 - Удалите одну из пар в словаре по существующему ключу из словаря my_dict и выведите значение из этой пары на экран.
  - Выведите на экран словарь my_dict.

3. Работа с множествами:
  - Создайте переменную my_set и присвойте ей множество, состоящее из разных типов данных с повторяющимися значениями.
  - Выведите на экран множество my_set (должны отобразиться только уникальные значения).
  - Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
  - Удалите один любой элемент из множества my_set.
  - Выведите на экран измененное множество my_set.

Примечания:
- Для вывода значений на экран используйте функцию print().
- Помните, что словарь и множество - неупорядоченные коллекции.
- Больше о методах словарей тут, множеств тут."""

print('Работа со словарями:')
my_dict = {'Pavel': 2000, 'Max': 2002, 'TestName': 1998}
print(my_dict)

print(my_dict['Max']) #Возвращает значение по существующему ключу
print(my_dict.get('Denis')) #Возвращает значение по отсутствующему ключу

my_dict['Alex'] = 1995 #Добавляет ключ и значение
my_dict['Idea'] = 1998 #Добавляет ключ и значение
print(my_dict)

print(my_dict.pop('TestName') ) #Согласно заданию - удаляем и после выводим на экран
print(my_dict) #Выведим на экран словарь

print('\nМножества')
my_set = {1, 3, 3, 2, 5, 4, 5, 1, 7, True, 12, 4, 5}
print(my_set)

my_set.add(23)
my_set.add(10)

my_set.discard(7)
print(my_set)