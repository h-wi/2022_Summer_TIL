from os import dup


l = list(map(str,input().split()))
for i in range(len(l)):

    check = [0,1,2,3,4,5,6,7,8,9]
    duplicated = False #중복되게 remove했는지 확인
    l1 = list(l[i]) #문자열로 받았기 때문에 리스트로 변환

    for j in range(len(l1)):
        try:
            check.remove(int(l1[j])) #중복되는 경우 value error 발생함
        except:
            duplicated = True 

    if not check and not duplicated: #check list가 비어있고 duplicated가 false일 경우
        l[i] = 'true'
    else:
        l[i] = 'false'
print(' '.join(l))