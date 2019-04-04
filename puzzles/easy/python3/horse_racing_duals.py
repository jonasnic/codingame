strengths = []
min_diff = 10000000
n = int(input())
for i in range(n):
    strengths.append(int(input()))

strengths.sort()

for i in range(n - 1):
    diff = strengths[i + 1] - strengths[i]
    min_diff = min(min_diff, diff)

print(min_diff)
