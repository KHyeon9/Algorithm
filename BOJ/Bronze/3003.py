arr = [1, 1, 2, 2, 2, 8]

result = list(map(int, input().split()))

for i in range(6):
    print(arr[i] - result[i], end=" ")