def is_palindrome(number):
    a = number // 1000
    b = (number // 100) % 10
    c = (number // 10) % 10
    d = number % 10

    if a == d and b == c:
        return True
    else:
        return False

number = int(input("Введите четырехзначное число: "))

if 1000 <= number <= 9999:
    if is_palindrome(number):
        print("Число настоящее.")
    else:
        print("Число кривое.")
else:
    print("Ошибка: Введите четырехзначное число.")
