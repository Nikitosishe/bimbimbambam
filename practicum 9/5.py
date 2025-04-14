def is_palindrome(s):
    return s == s[::-1]


for N in range(100000, 1000000):
    sN = str(N).zfill(6)
    sN1 = str(N + 1).zfill(6)
    sN2 = str(N + 2).zfill(6)
    sN3 = str(N + 3).zfill(6)

    if (is_palindrome(sN[-5:]) and
        is_palindrome(sN1[-5:]) and
        is_palindrome(sN2[1:5]) and
        is_palindrome(sN3)):
            print(N)