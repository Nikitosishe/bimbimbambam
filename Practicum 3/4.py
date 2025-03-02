rubles, kopecks, latte_number = map(int,input().split())
revenue_rubles = rubles * latte_number + kopecks * latte_number // 100
revenue_kopecks = kopecks * latte_number % 100
print(revenue_rubles,'руб.',revenue_kopecks,'коп.')