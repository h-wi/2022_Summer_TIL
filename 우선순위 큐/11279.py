import sys
import heapq

n = int(input())
max_heap = []
for i in range(n):
    num = int(sys.stdin.readline()) 
     #입력되는 자연수의 값이 너무 클땐 sys 모듈의 readline 함수 사용하기
    if num:
        heapq.heappush(max_heap,(-num,num)) 
        # heapq 모듈은 minheap만 구현됨, 튜플 형태로 마이너스 부호로 해싱하여 반대로                                
    elif len(max_heap) == 0:
        print(0)
    else: 
        print(heapq.heappop(max_heap)[1])
