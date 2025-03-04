nums = []

for i in range(0, 9):
    nums.append(int(input()))

max_num = max(nums)

print(f"{max_num}\n{nums.index(max_num) + 1}")