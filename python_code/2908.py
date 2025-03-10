A, B = input().split()
stack = []
tmp = ''

stack = list(A)
while len(stack):
    tmp += stack.pop()
A = int(tmp)
tmp = ''

stack = list(B)
while len(stack):
    tmp += stack.pop()
B = int(tmp)

print(A if A > B else B)