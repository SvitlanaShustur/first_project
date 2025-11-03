# 1 Створіть список на основі введеної послідовності цілих чисел і надрукуйте другу половину списку. Якщо кількість не парна, то вивести більшу кількість.
# value = "4 6 76 43 5 3 4 7 899"
# print(value)
# value_1ist = list(map(int,value.split(" ")))
# print(value_1ist[len(value_1ist)//2:])
# # n = len(value_1ist)
# print(n)
# m = value_1ist[n//2:]
# print(m)
# p = value_1ist[:n//2]
# print(p)

#---------------------------------------------------------------------------------

# 2 Створіть список на основі введеної послідовності цілих чисел і надрукуйте його елементи таким чином: два останні елементи переміщені з кінця в початок списку без зміни їх початкового порядку.

# value = "4 6 76 43 5 3 4 7 899"
# value_1ist = list(map(int,value.split(" ")))
# print(value_1ist)
# m = value_1ist[:-2]
# r = value_1ist[-2:]
# print(r + m)

#---------------------------------------------------------------------------------

# 3 Збережіть назви мов світу, які вводяться в одному рядку через пропуск, у списку. Простежте за тим, щоб елементи у списку не зберігались в алфавітному порядку. Відсортуйте список в алфавітному порядку і виведіть його елементи в рядку через пропуск.

# land = "England Ukraine Deutschland Spanisch Italie"
# land_list = land.split(" ") #створили список
# print(land_list)
# land_list_1 = land_list.copy() #зробили копію
# land_list.sort() # відсортували перший список
# print(land_list)

#---------------------------------------------------------------------------------

# 4. Виведіть елементи даного списку в зворотному порядку, не змінюючи сам список.
# land_list_2 = land_list_1[::-1] # зругий список вивели задом на перед
# print(land_list_2)

#---------------------------------------------------------------------------------

# 5. Виведіть всі елементи списку з парними індексами. Вводиться список чисел. Всі числа списку знаходяться на одному рядку.
# for i in range(0, len(land_list), 2):
#     print(i, end=" ")

# ind_land = ", ".join(str(i) for i in range(len(land_list)))
# print(ind_land)
# ind_2 = ind_land[::2]
# print(ind_2)
#---------------------------------------------------------------------------------

# 6.Bизначте, скільки різних слів у введеному рядку.

# Вхідні дані:

# New Delhi New York Paris Prague Reykjavik
# Happy New Year Happy New Year May we all have a vision now and then Of a world where every neighbor is a friend
# Вихідні дані:

# 6
# # 19
# text = "New Delhi New York Paris Prague Reykjavik"
# text = text.split() # зберегли у вигляді текст
# neu_text = []
# for word in text: # пройшлись по словах
#     # print(word)
# # for word_1 in range(len(text)):# пройшлись по символах
# #     print(word_1)
#     if word  not in neu_text:
#         neu_text.append(word)
# print(len(neu_text))

# text2 = "Happy New Year Happy New Year May we all have a vision now and then Of a world where every neighbor is a friend"
# text2 = text2.split() # зберегли у вигляді текст
# neu_text2 = []
# for word2 in text2: # пройшлись по словах
#     # print(word)
# # for word_1 in range(len(text)):# пройшлись по символах
# #     print(word_1)
#     if word2  not in neu_text2:
#         neu_text2.append(word2)
# print(len(neu_text2))
#---------------------------------------------------------------------------------
# [0, 1, 2, 3, 4, 5, 6]
# result = 0
# for wort_i in range(len(text)):
#     for i in range(wort_i + 1, len(text)):
#         if text[wort_i] == text[i]:
#              result -=1
#              break
# result_finall = result + 1
#---------------------------------------------------------------------------------

# 7. Напишіть програму, яка приймає послідовність чисел, розділених комами, від користувача і створює список і кортеж з цими числами.
# value = "5, 567,True, 2, f1"
# my_list = value.split(",")
# my_list_1 = list(my_list)
# my_tuple = tuple(my_list)
# print(my_list_1)
# print(my_tuple)
#---------------------------------------------------------------------------------

# # 9. Для введеної послідовності унікальних цілих чисел, поміняйте місцями мінімальний та максимальний елементи цієї послідовності. Надрукуйте отриманий список.
# def set_numbers(numbers):
#    min_index = numbers.index(min(numbers)) # шукаємо індекс мін числа
#    max_index = numbers.index(max(numbers)) # шукаємо індекс мах числа
#    numbers[max_index], numbers[min_index] = numbers[min_index], numbers[max_index]
#    return numbers

# numbers ="1 2 3 6 8 4 9 3 22 67 87"
# numbers = list(map(int, numbers.split()))

# print(numbers)
# print(set_numbers(numbers))

#---------------------------------------------------------------------------------
# 10. Напишіть програму, яка приймає послідовність рядків (порожній рядок для завершення програми) як вхідний рядок і друкує рядки у верхньому регістрі.

# Вхідні дані:

# python
# ruby
# go

# Вихідні дані:

# PYTHON
# RUBY
# GO

# while True: # варіант
#     line = input("Entre text: ")
#     if line == "":
#         break


# while input() != "": # варіант
#     print(1)


# a = "1" # варіант
# while a != "":
#     line = input("Entre text: ")
    
# a = "1"
# while a != "":
#     line = input("Entre text: ")

# run = True # варіант
# while run:
#     line = input("Entre text: ")
#     if line == "":
#         run = False
#     else:
#         result = line.upper()
#         print(result)

# while True: # рішення
#     line = input("Enter text: ")
#     if line == "":
#         break
#     print(line.upper())

#---------------------------------------------------------------------------------
# 11. У введеному списку цілих чисел, знайдіть і надрукуйте сусідні елементи, які мають однаковий знак. Якщо такої пари немає, не повинно нічого виводитися.

# Вхідні дані:

# 1 -2 -3 5 6 -3 7 8
# Вихідні дані:

# -2 -3
# 5 6
# 7 8

# numbers = [1, -2, -2, 5, 6, -3, 7, 8]
# print(type(numbers))

# for x in numbers:
#     x = 

# if n >= 0 and n + 1 >=0 n <= 0 and n + 1 <=0 or in number:
#     print(n, n+1)
# else:
#     print()
#---------------------------------------------------------------------------------

# 12.Напишіть програму для обчислення добутку цілих чисел (без використання циклу for), які вводяться через пропуск користувачем в одному рядку.

# Вхідні дані:

# 2 5 3
# Вихідні дані:

# 30

# numbers = list(map(int, input("Enter list: ").split()))
# # Var 1
# result = 1
# n = 0
# for n in numbers:
#     result *= n
#     n += 1
# print(f" Результат добутку складає {result}, кількість проходів {count}")
# # Var 2
# n = 0
# result = 1
# while n < len(numbers):
#     result *= numbers[n]
#     n +=1
# print(result, n)    
#---------------------------------------------------------------------------------
# 17. Користувач вводить два цілих додатних числа n і m. Напишіть програму, яка створює двовимірний масив розміром n x m і заповнює його символами . і * у шаховому порядку (як у вихідних даних). Лівий верхній кут повинен мати символ ..

# Вхідні дані:

# 6 8
# Вихідні дані:

# . * . * . * . *
# * . * . * . * .
# . * . * . * . *
# * . * . * . * .
# . * . * . * . *
# * . * . * . * .
# n = int(input("n: "))
# m = int(input("m: "))

# # for row in range(n):
# #     for col in range(m):
# #         if (row + col) % 2 == 0:
# #             print(".", end=" ") # виводить не в стовбчик, а в рядок
# #         else:
# #             print("*", end=" ")
# #     print("\n") # після закінчення кожного проходу циклу перериває рядок і починає друк з наступного рядка

# result = []
# for row in range(n):
#     m_list = []
#     for col in range(m):
#         if (row + col) % 2 == 0:
#             m_list.append(".") # виводить не в стовбчик, а в рядок
#         else:
#             m_list.append("*") #
#     result.append(m_list)
# print(result)
# range(n) -> від 0 до (n-1)
# range(k, n) від k до (n-1)
# range(k, n, s) від k до (n-1) з кроком s -> [k, k + s, k + s + s, ..., (n-1)]
