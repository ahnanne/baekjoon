T = int(input())

for i in range(0, T):
    answer = ''
    R, S = input().split()
    R = int(R)

    for s in S:
        answer += s * R

    print(answer)