A, B, V = map(int, input().split())

answer = (V - A) // (A - B)

if (V - A) % (A - B):
    answer += 2
else:
    answer +=1

print(answer)