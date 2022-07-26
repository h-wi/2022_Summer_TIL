f = open("sample.txt",'r')
lines = f.readlines()
f.close()

total = 0
for line in lines:
    score = int(line) #str을 int형으로 형변환
    total += score

average = total/len(lines)

f = open("result.txt",'w')
f.write(str(average)) #int를 str형으로 형변환
f.close()