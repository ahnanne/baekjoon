year = int(input())
is_leap = 0

# 연도가 4의 배수
if year % 4 == 0:
    if year % 100 != 0 or year % 400 == 0:
        is_leap = 1

print(is_leap)