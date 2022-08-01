n = int(input())
l1 = []
for i in range(n):
    age,name = map(str, input().split())
    l1.append([int(age),i,name])
l1.sort(key=lambda x: (x[0],x[1]))
for i in range(n):
    print("%s %s" % (l1[i][0],l1[i][2]))


