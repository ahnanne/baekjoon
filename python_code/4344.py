C = int(input())

for i in range(0, C):
    nums = list(map(int, input().split()))
    N = nums[0]
    score_list = nums[1:]

    average = 0

    for score in score_list:
        average += score

    average /= N

    cnt = 0

    for score in score_list:
        if score > average:
            cnt += 1

    print(f"{round(100 * cnt / N, 3)}%")