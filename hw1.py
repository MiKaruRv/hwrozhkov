#Задание 1:
num1 = int(input("Введите первое целое число: "))
num2 = int(input("Введите второе целое число: "))
num3 = int(input("Введите третье целое число: "))

if num1 <= num2 and num1 <= num3:
    min_number = num1
elif num2 <= num1 and num2 <= num3:
    min_number = num2
else:
    min_number = num3

print("Наименьшее число:", min_number)

#Задание 2:
num1 = int(input("Введите первое целое число: "))
num2 = int(input("Введите второе целое число: "))
num3 = int(input("Введите третье целое число: "))

if num1 == num2 == num3:
    result = 3
elif num1 == num2 or num1 == num3 or num2 == num3:
    result = 2
else:
    result = 0

print("Результат:", result)

#Задание 3:

my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
Сумма = sum(my_numbers)
print("Сумма всех чисел равна", Сумма)

#Задание 4:
my_array = [1, 0, 2, 0, 0, 3, 4, 0, 5, 0]

count = 0

for num in my_array:
    if num == 0:
        count += 1

print("Количество чисел, равных нулю:", count)

#Задание 5:
n = int(input("Введите натуральное число n (n <= 9): "))

if 1 <= n <= 9:
    for i in range(1, n + 1):
        for k in range(1, i + 1):
            print(k, end="")
        print()
else:
    print("Пожалуйста, введите натуральное число n в диапазоне от 1 до 9.")
#Задание 6:
n = int(input("Введите натуральное число n (n <= 9): "))

if n > 9 or n <= 0:
    print("Пожалуйста, введите натуральное число n в диапазоне от 1 до 9.")
else:

    for i in range(1, n + 1):

        for j in range(1, i + 1):
            print(j, end="")

        for k in range(i - 1, 0, -1):
            print(k, end="")
        print()

#Здание 7:
def countFrequency(my_list, x):
    count = 0

    for item in my_list:
        if item == x:
            count += 1

    return count
