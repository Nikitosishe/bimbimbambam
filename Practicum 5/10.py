pincode = int(input())
num1 = pincode // 1000
num2 = (pincode % 1000) // 100
num3 = ((pincode % 1000) % 100) // 10
num4 = (((pincode % 1000) % 100) % 10) % 10
if (pincode < 10000) and (pincode < 1900 or pincode > 2050):
    if num1 != num2 != num3 != num4:
        print("OK")
    else:
        print("ERROR")
else:
    print("ERROR")