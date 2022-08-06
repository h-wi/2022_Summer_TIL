n = list(input())
n.append('none') #마지막 요소에 garbage value를 추가해서 index error를 방지
s1 = ''
sum = 1 #문자는 1개 이상 주어지기 때문에 초깃값은 1
for i in range(len(n)-1): 
    if(n[i] == n[i+1]): #이웃 요소끼리 비교해서 같을 때만 카운트
        sum += 1
    else: # 다르면 i번째 요소의 문자와 sum을 s1 문자열에 업데이트 후
        s1 = s1 + n[i] + str(sum) 
        sum = 1 # 다시 초깃값을 설정
print(s1)
