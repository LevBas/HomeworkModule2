my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while index < len(my_list):
    if my_list[index] < 0:
        break
    elif my_list[index] >= 0:
        print(my_list[index])
    index = index + 1

# в условии задачи сказано, что нужно вывести все числа, пока не встретим отрицательное или пока список не закончится.
# учитывая заданный список, мы остановимся на "-5", но после него также есть положительные числа. Для того, чтобы вывести все положительные числа код должен быть:
#my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
#index = 0
#while index < len(my_list):
#    if my_list[index] >= 0:
#        print(my_list[index])
#    index = index + 1