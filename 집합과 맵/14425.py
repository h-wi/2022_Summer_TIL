n,m = map(int,input().split())

s1 = set() 
s2 = set()

for i in range(int(n)):
    str = input()
    s1.add(str)

for j in range(int(m)):
    str = input()
    s2.add(str)

l1 = list(s2)
sum = 0
for k in range(int(m)):
    print(k)
    if(l1[k] in s1):
        sum = sum + 1

print(sum)