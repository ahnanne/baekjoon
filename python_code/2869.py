A, B, V = map(int, input().split())

total = 0
days = 0

while total < V:
    # 낮
    total += A
    days += 1

    if total >= V:
        print(days)
    else:
        # 밤
        total -= B