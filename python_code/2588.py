import sys

numbers = []
for i in range(2):
    numbers.append(sys.stdin.readline().strip())

num1,num2 = numbers

for digit2 in reversed(num2):
    output = []
    extra = 0

    for digit1 in reversed(num1):
        multiple = int(digit2) * int(digit1)
        rest = multiple % 10
        
        if extra > 0:
            rest += extra

        extra = multiple // 10

        output.insert(0, rest)

    if extra > 0:
        output.insert(0, extra)

    print(int(''.join(map(str, output))))

print(int(num1) * int(num2))