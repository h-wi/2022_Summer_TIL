n = int(input())
l1 = []
result = []
for i in range(n):
    do = input()
    c = do.split(' ')[0]
    if c == 'push':
        l1.append(do.split(' ')[1])
    elif c == 'pop':
        try:
            result.append(l1.pop())
        except:
            result.append('-1')
    elif c == 'size':
        result.append(len(l1))
    elif c == 'empty':
        if len(l1) == 0:
            result.append('1')
        else:
            result.append('0')
    elif c == 'top':
        try:
            result.append(l1[len(l1)-1])
        except:
            result.append('-1')
for j in range(len(result)):
    print(result[j])