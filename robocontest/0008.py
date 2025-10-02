arr = list(map(int, input().split()))
arr.sort()

total = sum(arr)
min_sum = total - max(arr)
max_sum = total - min(arr)
print(min_sum, max_sum)