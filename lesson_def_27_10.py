#1 Напишіть функцію, яка отримує ім’я і друкує вітальне повідомлення Hello, <name>.
# name = "Oksana"
# def name_hello(name):
#     print(f"Hello, {name}!")
# name_hello(name) 
    
# def name_hello(name="NON"):
#     return f"Hello, {name}!"
    
# print(name_hello())
# print(name_hello(name))

#-----------------------------------------------------------------------------------------------------

#2 Напишіть функцію, яка отримує рядок і ціле число n та повертає n копій заданого рядка.
# def copy_string(text, n):
#     return (" " + text + " ") * n

# text = input("Enter text:")
# n = int(input("Enter n:")) 
# print(copy_string(text, n), end=" ")

#-----------------------------------------------------------------------------------------------------

#3 Напишіть функцію для обчислення суми двох цілих чисел.
# def sum_a_b(a, b):
#     return a + b 

# num_1 = int(input("Num_1: "))
# num_2 = int(input("Num_2: "))

# print(sum_a_b(num_2, num_1))

#4 Напишіть функцію для отримання рядка з перших n символів іншого рядка. Якщо довжина рядка менше n, поверніть початковий рядок.
# def n_letter(word, n):
#     if len(word) < n:
#         return word
#     else:
#         return word[:n]

# def n_letter(word, n):
#     if len(word) < n:
#         return word
#     return word[:n]
#     # print(1)

# string = "letter"
# n = 3
# print(n_letter(string, n))

#-----------------------------------------------------------------------------------------------------

# 5. Напишіть функцію для визначення найбільшого з трьох цілих чисел з використанянм вбудованої функції max().
# def number_max (number):
#     my_list = list(map(int, number.split()))
#     my_max = max(my_list)3

#     return my_max

# n1 = input("Enter n_1:")    
# n2 = input("Enter n_2:") 
# n3 = input("Enter n_3:") 

# data = " ".join([n1, n2, n3])
# result = number_max(data)
# print(result)

#-----------------------------------------------------------------------------------------------------

# 6. Напишіть функцію для створення позначок тегів HTML навколо введених рядків. Функція отримує назву тега HTML і рядок, який необхідно помістити у відповідні теги.
# def teg_html (teg, text):
#     return f"<{teg}>{text}</{teg}>"
# text = input("Enter text: ")
# #1
# # teg, string = text.split()
# #2
# teg = text.split()[0]
# string = " ".join(text.split()[1:])

# print(teg_html (teg, string))

#-----------------------------------------------------------------------------------------------------

# 7. Напишіть функцію, яка повертає назву пори року для введеного значення номера місяця.

# def month_output(number):
#         months = [
#         "Jan", "Feb", "Mar", "Apr", "Mai", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov", "Des"
#         ]
#         if 1<= number <= 12:
#               return months[number-1]
#         else:
#               return "помилка в номері місяця"
    
#     monthe_num = int(input("Введіть номер місяця: "))
# print(month_output(monthe_num))

#-----------------------------------------------------------------------------------------------------

# 8 Напишіть функцію для створення гістограми (наприклад, у вигляді *) із заданого списку цілих чисел як у вихідних даних. Формат введення списку чисел як у вхідних даних.

# Вхідні дані:

# 2,7,1,4,2,3,9,3
# Вихідні дані:

# **
# *******
# *
# ****
# **
# ***
# *********
# ***

# def my_gisto(input_num):
#     numbers = list(map(int,input_num.split(",")))
#     for i in numbers:
#         print("*" * i) # чому не ме працює тут return

# num_output = input("Введіть числа через кому: ")
# my_gisto(num_output)

#-----------------------------------------------------------------------------------------------------

#10 Напишіть функцію, яка отримує значення середньомісячної кількості опадів по місяцях (в мм) і повертає загальний обсяг опадів протягом року, середньорічну кількість опадів, назви місяців та значення з найвищим та найменшим числом опадів протягом року.

# Вхідні дані:

# 22 22 24 49 72 98 101 82 51 40 36 24
# Вихідні дані:

# (621.0, 51.75, (101.0, 'July'), (22.0, 'January'))

# def rainfall_statistics(values):
#     months = [
#         "Jan", "Feb", "Mar", "Apr", "Mai", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov", "Des"
#         ]
#     rain =list(map(float, values.split()))
#     total = sum(rain)
#     average = total / len(rain)
#     max_rain = max(rain)
#     min_rain = min(rain)

#     max_month = months[rain.index(max_rain)]
#     min_month = months[rain.index(min_rain)]

#     return (total, average, (max_rain, max_month), (min_rain, min_month))

# data = "22 22 24 49 72 98 101 82 51 40 36 24"
# result = rainfall_statistics(data)

# print(result)

#-----------------------------------------------------------------------------------------------------

# 11 На стадіоні є три категорії місць для сидіння: місця класу A коштують a грошових одиниць, місця класу B коштують b грошових одиниць, а місця класу C - c грошових одиниць. Напишіть першу функцію, яка запитує скільки продано квитків на кожний клас місць, і другу функцію, яка відображає суму отриманого доходу від продажу квитків на кожен клас окремо і загалом. Формати введення і виведення такі, як у вхідних і вихідних даних.

# Вхідні дані:

# A
# 20.50
# 45
# B
# 15.75
# 30
# C
# 10.55
# 15
# Вихідні дані:

# ({'A': 922.5, 'B': 472.5, 'C': 158.25}, 1553.25)

def number_tickets(a, b, c):
    ticket_a = a
    ticket_b = b
    ticket_c = c
    total = a + b +c
    
    print(ticket_a)
    print(ticket_b)
    print(ticket_c)
    return total

# def sum_tickets(sam_)
тт

amount_ticket_a = int(input("Введіть числа куплених місць класу А: "))
amount_ticket_b = int(input("Введіть числа куплених місць класу B: "))
amount_ticket_c = int(input("Введіть числа куплених місць класу C: "))

total_tickets = number_tickets(amount_ticket_a, amount_ticket_b, amount_ticket_c)
print(total_tickets)