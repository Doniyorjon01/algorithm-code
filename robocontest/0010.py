n = int(input())
a, b, c = map(int, input().split())
total = a + b + c
if total >= n:
    print("No")
else:
    print("Yes")