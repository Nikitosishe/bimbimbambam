for i in range(10, 100):
    number = str(i)
    proizvdenie = str(i ** 2)
    if len(proizvdenie) == 3:
        if proizvdenie[0] != number[0] or number[1]:
            if proizvdenie[1] == number[0]:
                if proizvdenie[2] == number[1]:
                    print(proizvdenie)