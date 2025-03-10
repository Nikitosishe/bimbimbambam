score_1, score_2, score_3 = map(int,input().split())
if score_1 >= score_2 and score_1 >= score_3:
    print(score_1)
elif score_2 >= score_1 and score_2 >= score_3:
    print(score_2)
elif score_3 >= score_1 and score_3 >= score_2:
    print(score_3)