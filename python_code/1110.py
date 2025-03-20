N = input()
M = N

cycle = 0

while True:
    cycle += 1

    if len(M) < 2:
        M = '0' + M

    s = int(M[0]) + int(M[1])
    M = M[1] + str(s)[-1]

    if M == N or M == '0' + N:
        break

print(cycle)