class maxheap():
    lst = [0] # max는 1번째 인덱스여야한다 (나눗셈 몫 사용)

    def heap_insert(self,data):
        self.lst.append(data)
        i = len(self.lst) - 1   #추가 된 노드의 인덱스
        while((i != 1) and (data > self.lst[i//2])):
            self.lst[i] = self.lst[i//2] # 부모 노드의 인덱스는 자식 인덱스를 2로나눈 몫
            i = i // 2
        self.lst[i] = data

    def heap_delete(self):
        if len(self.lst) == 1: # heap이 empty하면 0을 반환
            return 0
        res = self.lst[1] # 최고값 저장
        tmp = self.lst[len(self.lst)-1] # pop하여 마지막 값을 저장
        parent = 1 # 부모 : 0번 인덱스
        child = 2 # 자식 : 1번,2번 인덱스

        while (child <= len(self.lst)-1):
            if((child< len(self.lst)-1) and self.lst[child]<self.lst[child+1]):
                child += 1 #child가 힙의 범위 안 and "오른쪽 자식이 더 크면"
            if (tmp >= self.lst[child]):
                break
            self.lst[parent] = self.lst[child]
            parent = child #더 밑으로 가서 탐색
            child *= 2
        self.lst[parent] = tmp
        self.lst.pop()
        return res

n = int(input())
heap = maxheap()
result = []
for i in range(n):
    data = int(input())
    if data:
        heap.heap_insert(data)
    else:
        print(heap.heap_delete())
