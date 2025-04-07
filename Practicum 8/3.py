number_of_people = 0
total_income = 0
while (i := int(input())) != 0:
    number_of_people += 1
    total_income += i
print(total_income / number_of_people)