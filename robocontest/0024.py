h, m, s = map(int, input().split())
h1, m1, s1 = map(int, input().split())
total1 = h*3600+m*60+s
total2 = h1*3600+m1*60+s1
print(total2-total1)