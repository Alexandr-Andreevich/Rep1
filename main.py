


# number = int(input("Введите длину списка: "))
# print(f'Введите {number} любых числа')
#
# spisok = []
#
# for i in range(number):
#     spisok.append(int(input()))
#
# for i in range(number):
#     if spisok[i-1] < spisok[i] > spisok[i+1]:
#         print('Yes')
#         break
#     else:
#         print('No')
#         break



# number = int(input("Введите длину списка: "))
# print(f'Введите {number} любых числа')
#
# spisok = []
#
# for i in range(number):
#     spisok.append(int(input()))
#
# spisok = sorted(spisok)
#
# for i in range(number//2):
#     if not spisok[i] < spisok[i+1+number//2] > spisok[i+1]:
#         print('No')
#         break
# else:
#     print('Yes')


a = 17 // (23 % 7)
b = 34 % a * 5 - 29 % 4 * 3
print(a * b)