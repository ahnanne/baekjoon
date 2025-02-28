N,X = map(int, input().split())

nums = map(int, input().split())
answer = []

for num in nums:
    if num < X:
        answer.append(num)

print(' '.join(map(str, answer)))