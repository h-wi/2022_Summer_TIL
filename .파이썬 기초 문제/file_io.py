f = open("newfile.txt",'w')
for i in range(1,11):
    data = "%d line\n" % i
    f.write(data) #파일 입력 ('w)
f.close() 

f = open("newfile.txt",'r') 
line = f.read() #모든 라인을 문자열로 출력 ('r')
#line = f.readline() , 한 라인만 출력
#line = f.readlines(), 모든 라인을 리스트로 출력
print(line)
f.close()
 
f = open("newfile.txt",'a') #파일에 추가 입력 ('a')
for i in range(11,20):
    data = "%d line\n" % i
    f.write(data)
f.close

with open("newfile.txt",'a') as f:
    f.write("Life is too short, you need Python")
# with문으로 자동으로 f.close()를 실행 할수도 있다.
