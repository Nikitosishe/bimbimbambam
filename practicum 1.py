#1
print("Hello, Python!\n")

#2
print("Привет, Python!")
print("Hello, Python!")
print("Bonjour Python!")
print("Hej, Python!")
print("Hola, Python!\n")

#3
print("Привет Python!\n", sep=' ')

#4
print("(\\___/)")
print("(='.'=)")
print("(\")_(\")\n")

#5
print("Привет, Python!", "Hello, Python!", "Bonjour Python!", "Hej, Python!", "Hola, Python!", sep = '\n')

#6
print('Как вас зовут?')
name = input()
print('Здравствуйте,', name)

#7
print('Как вас зовут?')
name = input()
print('Здравствуйте,', name)
print('Что вам нравится?')
entertainment = input()
print('Отлично!', entertainment, '- отличное увлечение!')

#8
print('Login:')
login = input()
print('Password:')
password = input()
print('New password:')
new_password = input()
print('User', login, "has changed the password to", new_password)

#9
print('Введите плей-лист папы:')
song1 = input()
song2 = input()
song3 = input()
song4 = input()
song5 = input()
print('Плей-лист мамы:')
print(song5)
print(song4)
print(song3)
print(song2)
print(song1)

#10
print('Номер рейса:')
flight_number = input()
print('Название авиакомпании (на русском языке):')
organization_name_rus = input()
print('Название авиакомпании (на английском языке):')
organization_name_eng = input()
print('Город прилета (на русском языке):')
city_rus = input()
print('Город прилета (на английском языке):')
city_eng = input()
print('Заканчивается посадка на рейс', flight_number, organization_name_rus, 'до', city_rus)
print('This is the final boarding call for', organization_name_eng, 'flight', flight_number, 'to', city_eng)

#11
print('Как вас зовут?')
name2 = input()
print(f'Привет, {name2}!')

#12
cost_sell = int(input())
print((cost_sell-(96 * 48))/(96/16))

#13
import math as math
blind_zone = int(input())
reception_radius = int(input())
print(abs(math.pi*reception_radius**2 - math.pi*blind_zone**2   ))

#14
number1 = int(input())
print(float(number1 - 4))

#15
number_1 = float(input())
print(number_1 / 91.44, 'ярдов')
print(number_1 / 160934.4, 'мили')
print(number_1 / 30.48, 'футов')
print(number_1 / 2.54, 'дюймов')
