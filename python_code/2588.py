num1 = input()
num2 = input()

for digit2 in reversed(num2):
    output = []
    extra = 0

    for digit1 in reversed(num1):
        multiple = int(digit2) * int(digit1)
        rest = (multiple + extra) % 10
        extra = (multiple + extra) // 10

        output.insert(0, rest)

    if extra > 0:
        output.insert(0, extra)

    print(int(''.join(map(str, output))))

print(int(num1) * int(num2))