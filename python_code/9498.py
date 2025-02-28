score = int(input())

if score >= 80:
    if score >= 90:
        print('A')
    else:
        print('B')
else:
    if score < 60:
        print('F')
    elif score < 70:
        print('D')
    else:
        print('C')