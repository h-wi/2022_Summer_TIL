n = int(input())
l1 = [] #모든 연산에 대해 big-oh = O(1) 
front = 0
for i in range(n):
    do = input()
    if do[0:4] == 'push':
        l1.append(do[len(do)-1])
    elif do[0:3] == 'pop':
        try:
            print(l1[front])
            front += 1
            #print(l1.pop(0)) pop의 연산복잡도 맨 마지막은 O(1)이지만 특정 인덱스는 O(n), 제거된 값 이후로 다 요소들을 앞으로 재배치하기 때문에
        except:
            print('-1')
    elif do[0:4] == 'size':
        print(len(l1)-front) #len의 연산복잡도 O(1)
    elif do[0:5] == 'empty':
        if len(l1)-front == 0: 
            print('1')
        else:
            print('0')
    elif do[0:5] == 'front':
        try:
            print(l1[front]) #O(1)
        except:
            print('-1')
    elif do[0:4] == 'back':
        try:
            print(l1[len(l1)-1]) #O(1)
        except:
