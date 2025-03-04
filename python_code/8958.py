N = int(input())

for i in range(0, N):
    res = input()
    consec = 0
    total = 0

    for c in res:
        if c == 'O':
            consec += 1
        else:
            consec = 0

        total += consec

    print(total)