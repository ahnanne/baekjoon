A = int(input())
B = int(input())
C = int(input())

total = str(A * B * C)

for i in range(0, 10):
    cnt = 0

    for num in total:
        if num == f"{i}":
            cnt += 1

    print(cnt)