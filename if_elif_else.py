# Розгалудження

# Напишіть програму, в якій користувач вводить пароль і якщо він співпадає із наперед визначеним паролем для цього користувача, то виводиться повідомлення Password accepted.. У іншому випадку повідомлення буде Sorry, that is the wrong password..
# password = input("Enter password: ")
# password_accept = "QwErTy"
# if password == password_accept:
#     print("Password accepted.")
# else: 
#     print("Sorry, that is the wrong password.")

# Користувачем вводиться два імені. Використовуючи конструкцію розгалуження програма повинна вивести імена в алфавітному порядку.
# name1 = input("Enter name1: ")
# name2 = input("Enter name2: ")
# варіант 1
# if name1 <= name2:
#     print(name1,name2)
# else:
    # print(name2,name1)
# варіант 2
# if name1 <= name2:
#     print(name1,name2)
#     name1, name2 = name2, name1
# print(name2,name1)

# Напишіть програму, яка виводить назви введених чисел. Користувач вводить ціле число. Якщо це число або 1 або 2 або 3, то виводиться повідомлення - назва числа, відповідно, One, Two, Three. В усіх інших випадках виводиться слово Unknown.

# name = input("Enter name: ")
# name_of_number = "" # звертаємо умову, коли створюється змінна
# if name_of_number == 1:
#     name_of_number = "One"
# elif name_of_number == 2:
#     name_of_number = "Two"
# elif name_of_number == 3:
#     name_of_number = "Three"
# else:
#     name_of_number = "Unknow"
# print(name_of_number)

# # Користувач вводить дві різних англійські літери в окремих рядках. Напишіть програму, яка виводить повідомлення про місце розташування однієї літери відносно іншої у алфавіті.
# letter1 = input("Enter letter1: ").lower()
# letter2 = input("Enter letter2: ").lower()
# if letter1 <= letter2:
#     print("First letter:", letter1, "Second letter:", letter2)
# else:
#     print("First letter:", letter2, "Second letter:", letter1)

# Якщо регістр важливий
# letter1 = input("Enter letter1: ")
# letter2 = input("Enter letter2: ")

# if letter1.lower() == letter2.lower():
#     if letter1 < letter2:
#         print("First letter:", letter1, "Second letter:", letter2)
#     else:
#         print("First letter:", letter2, "Second letter:", letter1)
# elif letter1.lower() < letter2.lower():
#     print("First letter:", letter1, "Second letter:", letter2)
# else:
#     print("First letter:", letter2, "Second letter:", letter1)

# 5. Напишіть програму, в якій користувач вводить значення температури, і, якщо це значення менше або дорівнює 0 градусів Цельсія, необхідно вивести повідомлення A cold, isn’t it?. Якщо ж температура становить більше 0 і менше 10 градусів Цельсія повідомлення буде Cool., у інших випадках Nice weather we’re having..
# i = float(input("Enter Temperatur: "))
# if i <= 0:
#     print("A cold, isn’t it?")
# elif i > 0 and i < 10:
#     print("Cool")
# else:
#     print("Nice weather we’re having")

    
# Середній рівень

# Визначте назву геометричної фігури за введеною кількістю її сторін. Програма повинна підтримувати фігури від 3 до 6 сторін. Якщо введена кількість сторін поза межами цього діапазону, програма повинна відображати відповідне повідомлення.
# number_of_sides = int(input("Enter the number of sides of the shape: "))
# if number_of_sides == 3:
#      print("The figure is called a triangle.")
# elif number_of_sides == 4:
#      print("The shape is called a square.")
# elif number_of_sides == 5:
#      print("The figure is called a pentagon.")
# elif number_of_sides == 6:
#      print("The figure is called a hexagon.")
# else:
#     print("I don't know the name of this figure.")


# Ігрове поле рулетки поділено на номери від 0 до 36, які мають чорний, червоний або зелений кольори. Номер 0 має зелений колір, для номерів від 1 до 10, непарні номери - червоні, а парні - чорні. Непарні номери від 11 до 18 - чорні, а парні номери - червоні. Непарні номери від 19 до 28 - червоні, а парні номери - чорні. Непарні номери від 29 до 36 - чорні, а парні номери - червоні. Напишіть програму, яка отримує номер (число від 0 до 36) та показує, чи є номер зеленим, червоним або чорним. Програма повинна враховувати варіант, якщо користувач вводить номер, який знаходиться за межами діапазону від 0 до 36.
# nummer =  int(input("Enter the number : "))
# if nummer == 0:
#      print("ваше число зелене")
# elif nummer >= 1 and nummer <= 10:
#     if nummer % 2 == 0:
#          print("ваше число чорне") 
#     else:
#          print("ваше число червоне")
# elif nummer >= 11 and nummer <= 18:
#     if nummer % 2 == 0:
#          print("ваше число червоне") 
#     else:
#          print("ваше число чорне")
# elif nummer >= 19 and nummer <= 28:
#     if nummer % 2 == 0:
#          print("ваше число чорне") 
#     else:
#          print("ваше число червоне")
# elif nummer >= 29 and nummer <= 36:
#     if nummer % 2 == 0:
#          print("ваше число червоне") 
#     else:
#          print("ваше число чорне")
# else:
#      print("Такого поля не існує")


# Дано дві точки: A (x1, y1) і B (x2, y2). Напишіть програму, яка визначає, яка із точок знаходиться далі від початку координат.
# x1 =  int(input("Enter x1 : "))
# y1 =  int(input("Enter y1 : "))
# x2 =  int(input("Enter x2 : "))
# y2 =  int(input("Enter y2 : "))
# if (x1 ** 2 + y1 ** 2)**(1/2) > (x2 ** 2 + y2 ** 2)**(1/2):
#     print("Точка А знаходиться далі, ніж точка В, від початку кооординат")
# elif (x1 ** 2 + y1 ** 2)**(1/2) == (x2 ** 2 + y2 ** 2)**(1/2):
#     print("Точка А та точка В знаходяться на однаковій відстані від початку координат")
# else:
#     print("Точка B знаходиться далі, ніж точка A, від початку кооординат")
    
#  Вхідні дані:
#  1
#  2
#  3
#  2
#  4
#  4
#  4
#  4



#  Вихідні дані:
#  B
#  The distance is the same 
# Вводяться координати (x, y) точки A і радіус кола (r). Визначити, чи належить дана точка колу, якщо його центр знаходиться в початку координат.
# Вхідні дані:
# 3
# 4
# 5
# -2
# 5
# 3



# Вихідні дані:
# The point belongs to the circle
# The point is outside the circle
# Дано натуральное число. Визначити, чи закінчується число парною цифрою.
# Вхідні дані:
# 1234
# 35
# Вихідні дані:
# True
# False