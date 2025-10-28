# nummer_punkt = input("=== Помічник користувача ===\n"
#     "1 — Перевірити пароль\n"
#     "2 — Обчислити середній бал\n"
#     "3 — Перевірити слово на паліндром\n"
#     "4 — Вийти\n"
#     "Введіть пункт меню: ")

# while nummer_punkt == 1:
#-----------------------------------------------------------------------
# password = input("Введіть пароль: ")
# word_length = len(password)
# password_k = password.isupper() # перевіряємо наявність маленьких літер
# password_g = password.islower() # перевіряємо наявність великих літер
# password_z = password.isdigit() # перевіряємо чи це цифровий рядок
# password_z_l = password.isalpha() # перевіряємл чи не буквений рядок
# # print(word_length)
# # print(password_k)
# # print(password_g)
# # print(password_z)
# if " " in password:
#     print("Пароль не має містити пробіли")
# elif word_length < 8:
#     print("Пароль має містити не менше 8 символів")
# elif password_k == True:
#     print("Пароль має містити хоча б одну маленьку букву")
# elif password_g == True:
#     print("Пароль має містити хоча б одну велику букву")
# elif password_z == True:
#     print("Пароль має містити також і маленькі, і великі букви")
# elif password_z_l == True:
#     print("Пароль має містити хоча б одну літеру]")
# else:
#     print(f"{password} Пароль надійний")
# ----------------------------------------------------------------------
ball = input("Введіть свої бали через кому:")
number = [int(x) for x in ball.split(",")]
print(number)
n = len(number)
for b in number:
    if b > 12:
        print("Балл може бути від 1 до 12")
average = sum(number)/n
print(average)








