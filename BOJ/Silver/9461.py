for _ in range(int(input())):
    n = int(input())
    arr = [0, 1, 1]
    for i in range(3, n + 1):
        arr.append(arr[i - 3] + arr[i - 2])
    print(arr[-1])