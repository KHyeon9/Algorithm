n = int(input())
nums = list(map(int, input().split()))
res = 0

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if nums[i] * nums[j] == nums[k]:
                res += 1
print(res)