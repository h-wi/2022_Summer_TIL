n = int(input())
result = []
for i in range(n):
    string = input()
    stack = []
    for j in range(len(string)):
        if string[j] == '(':
            stack.append(string[j])
        else:
            if len(stack) == 0:
                stack.append(string[j])
                break
            else:
                stack.pop()
    if not stack:
        result.append('YES')
    else:
        result.append('NO')
for j in range(n):
    print(result[j])
        
