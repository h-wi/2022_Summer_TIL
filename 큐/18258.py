n = int(input())
l1 = [] #모든 연산에 대해 big-oh = O(1) 
for i in range(n):
    do = input()
    c = do.split(' ')[0] #split의 연산복잡도? 명령어는 짧다.
    if c == 'push':
        l1.append(do.split(' ')[1])
    elif c == 'pop':
        try:
            print(l1[0])
            l1 = l1[1:]
            #print(l1.pop(0)) pop의 연산복잡도 맨 마지막은 O(1)이지만 특정 인덱스는 O(n), 제거된 값 이후로 다 요소들을 앞으로 재배치하기 때문에
            #리스트로 구현하기 어려움.
        except:
            print('-1')
    elif c == 'size':
        print(len(l1)) #len의 연산복잡도 O(1)
    elif c == 'empty':
        if len(l1) == 0: 
            print('1')
        else:
            print('0')
    elif c == 'front':
        try:
            print(l1[0]) #O(1)
        except:
            print('-1')
    elif c == 'back':
        try:
            print(l1[len(l1)-1]) #O(1)
        except:
            print('-1')
