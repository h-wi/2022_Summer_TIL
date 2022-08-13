# TIL
* Python 학습서 : 박응용, 점프 투 파이썬(2019)

~~* Springboot 학습서 : 이동욱, 스프링 부트와 AWS로 혼자 구현하는 웹 서비스(2019)~~

백준 코딩테스트 학습(C,Python) 및 ~~백엔드 스터디~~
# 2022.07.09
계획 
1. VScode 및 InteliJ 설치 및 개발 환경 설정 
2. 코딩테스트 학습 계획 수립
## VScode C언어 구동환경 설정
<img width="909" alt="image" src="https://user-images.githubusercontent.com/108285793/178094310-eca3e196-3a1c-4f98-aef8-fe02d5508f65.png">
참고 : https://evandde.github.io/vscode-cpp/

* 백엔드 학습을 위한 InteliJ 설치 및 개발 환경 설정
인텔리제이 설치 후, 프로젝트 파일을 만들면 그레이들 프로젝트로 설정됨
스프링 부트 프로젝트로 변경이 필요.

```java
buildscript {
    ext {
        springBootVersion = '2.1.9.RELEASE'
    }
    repositories {
        mavenCentral()
        jcenter()
    }
    dependencies {
        classpath("org.springframework.boot:spring-boot-gradle-plugin:${springBootVersion}")
    }
}
```
* mavenCentral은 라이브러리 업로드를 위해서는 많은 설정이 필요
jcenter를 repositories에 추가하여 자동화가 용이하게 설정.

* 스프링 부트 개발을 위해 dependencies로 string-boot-start-web과 string-boot-start-test 받아오기 설정.

<img width="799" alt="image" src="https://user-images.githubusercontent.com/108285793/178094739-be194778-664c-4575-80c7-10e97faddd26.png">
의존성을 모두 불러와서 개발환경 구축 성공.
책의 예제는 모두 스프링 부트 2.1.x가 기준이여서 모두 2.1.18로 변경 -> 2.1.x 버전은 자바 JDK 8 버전 필요
<img width="685" alt="image" src="https://user-images.githubusercontent.com/108285793/178094893-875ca4c9-b9e0-4bad-818e-8ec61f09f3ee.png">
그레이들 버전 또한 4.x 버전으로 변경 완료.

## 코딩테스트 학습 계획 수립

매주 모임마다 각 팀원별로 일주일동안 공부한 문제 리뷰 


백준 단계별로 풀어보기에서 풀어보고 싶은 단계 의견 수렴.
조원별로 단계별 섹터를 나눠서 풀고 싶은 문제를 풀고 모임때마다 리뷰를 통해 함께 학습

+ 김태휘: 재귀, 브루트포스, 정렬, 스택, 큐, 분할정복, 이분탐색, 그래프와 순회, 트리

+ 최경주: 백트래킹, 분할 정복, 그래프와 순회, 최단경로 역추적, 세그먼트 트리, 집합과 맵

+ 김민규: 큐, 그래프와순회, 정렬, 우선순위큐, 분할정복, 이분탐색, 최단경로

<hr/>
1주차 소감

->예상보다 학습해야할 양이 많았다. 
그래서 목표를 너무 크게 잡으면 중간에 포기하기 쉬우니

차근차근 현실적으로 할 수 있는 목표로 수정했다.
<hr/>

# 2022.07.18
Python 학습 및 백준 단계별 풀이 (재귀)

## Python의 자료형과 문자열 포매팅
* Python에서의 새로운 연산 (숫자)
```python
a=4
b=4
a ** b #지수

b=5
a // b #나눗셈 후 소수점 버리는 연산

c="Life is good"
print(c[0:3]) #Life, 슬라이싱
```

* 문자열 수정하기
```python
a="Pithon"
a[1]='y'

a[:1]+'y'+a[2:] #Python
```
수정 불가능. 문자열은 immutable한 자료형 !
슬라이싱을 이용한다

* 문자열 포매팅

포매팅=서식 서식자료형은 같지만 문법이 다른 언어와 달랐다.
```python
"I eat %d apples." % 3 
"I ate %d apples. so I was sick for %d days." % (number,day)
```

* 문자열 관련 함수 (문자열)

```python

a="hobby"
a.count('b') #2 b의 개수 반환

a="Python is best choice"
a.find('b') #10 b가 처음 나온 위치(index) 반환
a.find('k') #-1 해당 값이 없으면 -1을 반환
a.index('k') # 해당 값이 없으면 오류 발생

a=","
a.join("abcd") #'a,b,c,d'

a="hi"
a.upper() # HI
a.lower() # hi

a="Life is too short"
a.replace("Life","Your leg") # Your leg is too short

a.split() # 공백을 기준으로 문자열 나누기 (Your,leg,is..)
a="a:b:c:d"
a.split(:) # : 기호를 기준으로 문자열 나누기(a,b,c,d)
```

## 백준 단계별 풀어보기 (재귀)
* 재귀함수가 뭔가요? , 문제번호 : 17478
```C
#include <stdio.h>

void question(int n,int j)
{
    int i=0;
    while(i<j) {printf("____"); i++;}
    if (i!=0) i=0;
    printf("\"재귀함수가 뭔가요?\"\n");
    if(n==0)
    {
        while(i<j) {printf("____"); i++;}
        if (i!=0) i=0;
        printf("\"재귀함수는 자기 자신을 호출하는 함수라네\"\n");
    }
    else {
        while(i<j) {printf("____"); i++;}
        if (i!=0) i=0;
        printf("\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.\n");
        while(i<j) {printf("____"); i++;}
        if (i!=0) i=0;
        printf("마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.\n");
        while(i<j) {printf("____"); i++;}
        if (i!=0) i=0;
        printf("그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"\n");
        question(n-1,j+1);
    }
    while(i<j) {printf("____"); i++;}
        if (i!=0) i=0;
    printf("라고 답변하였지.\n");
}

int main()
{
    int n,j=0;
    scanf("%d",&n);
    printf("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.\n");    
    question(n,j);
    return 0;
}
```
간단한 문제였지만 언더바 4개를 출력해야 하는 부분이 인상적이었다.

재귀 함수인 question의 매개변수인 n은 재귀가 진행될 수록 값이 줄어들어 언더바를 4의 배수로 출력하는 게 쉽지 않았는데,

매개변수 j를 추가해서 언더바 출력을 구현했다. 

* 별 찍기 - 10 , 문제번호 : 2447 ~

3x3 패턴으로 계속 이어 붙일려고 했지만 행으로 이어 붙이는 방법을 찾지 못했다.

<img width="389" alt="image" src="https://user-images.githubusercontent.com/108285793/179714442-48f86845-a084-4596-b98b-73450913ada1.png">
<img width="176" alt="image" src="https://user-images.githubusercontent.com/108285793/179714589-d588eda5-d105-4342-8dd8-ed90f62923ed.png">

```C
void stars(int n)
{
    int i,j=1;
    for(i=1;i<=n;i++)
    {
        for(j=1;j<=n;j++)
        {
            if(i>(n/3)&&i<=n-(n/3)&&
                 j>(n/3)&&j<=n-(n/3))
            {
                printf(" ");
                continue;
            }
            if(n==3)
                printf("*");
            else 
                stars(n/3);
        }
        printf("\n");
    }
}
```
~~삽질~~

동적 할당으로 배열을 만들고 이중 for문으로 출력하는 게 나을 듯.

# 2022.07.19
## 2447 나머지 풀기

이중 for문과 재귀를 같이 사용하니 n(=27,81..)이 커질 때 시간이 너무 오래걸렸다.

규칙성을 찾으니 배열을 쓸 필요가 없었다. 별 찍기 문제는 규칙성을 찾는게 가장 중요한듯

구글링으로 공백이 나오는 지점의 규칙성을 파악하니 쉽게 풀렸다.

```C
//참고 : https://hou27.tistory.com/entry/BaekjoonC%EC%96%B8%EC%96%B4-2447%EB%B2%88-%EB%B3%84%EC%B0%8D%EA%B8%B0-10
#include <stdio.h>

void stars(int i,int j,int n)
{
   if((i/n)%3==1&&(j/n)%3==1)
   {
        printf(" ");
   }
   else
   {
        if (n/3==0)
            printf("*");
        else 
        {
            stars(i,j,n/3);
        }
   }
}

int main()
{
    int n=0;
    scanf("%d",&n);

    for(int i=0; i<n; i++)
    {
        for(int j=0; j<n; j++)
        {
            stars(i,j,n);
        }
        printf("\n");
    }
    return 0;
}
```
# 2022.07.20

* 모각소 2주차 모임 

Python 문법 배우기 및 백준 브루트 포스 알고리즘 문제 풀기

## 블랙잭(2798), 분해합(2231)
```C
#include <stdio.h>
// 브루트 포스, 블랙잭(2798)
int main()
{
    int len,n=0;
    scanf("%d %d",&len,&n);
    int cards[len];
    for(int i=0;i<len;i++)
    {
        scanf("%d",&cards[i]);
    }

    int max=0;
    int sum=0;
    for(int i=0;i<len-2;i++) //3개의 카드의 경우의 수를 계산하므로 처음부터 뒤에서 2번째까지
    {
        for(int j=i+1;j<len-1;j++) // i 다음 번의 index부터 뒤에서 1번째까지 탐색
        {
            for(int k=j+1;k<len;k++) // j 다음 번의 index부터 끝까지
            {
                sum=cards[i]+cards[j]+cards[k];
                if(sum>max && sum<=n) //입력된 수보다 작은 값만 max에 대입
                    max = sum;
            }
        }
    }
    printf("%d\n",max);
    return 0;
}
```
```C
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char n[7];
    scanf("%s",n);  //문자열로 정수를 입력받아 자릿수 파악 빠르게

    int sum=0; int tmp;
    int len=strlen(n); //strlen 함수 사용
    int min=__INT_MAX__;

    for(int i=0;i<atoi(n);i++) //0부터 분해합 전까지 경우의 수 계산
    {
        sum += i; 
        tmp=i;
        while(tmp!=0) //i의 각 자릿수를 덧셈해주는 반복문
        {
            sum += tmp%10; 
            tmp = tmp/10;
        }
        if (sum==atoi(n)&&sum<min) //sum이 입력값과 같고 min보다 작다면
            min = i;
        sum = 0;
    }
    if(min==__INT_MAX__) // 생성자가 없는 경우
        printf("0\n");
    else        
        printf("%d\n",min);
    return 0;
}
```
## Python 자료형

### 리스트 (List)
1. 순서가 있다.
2. 리스트의 요소는 어떠한 자료형도 포함할 수 있다. (정수,문자열,리스트...)
3. 요소 값들은 중복될 수 있다.

* 중첩 리스트의 인덱싱
```Python
a=[1,2,3,['a','b','c']]

a[0] #1
a[-1] #['a','b','c']
a[3][0] #'a'
```
* 리스트에서의 슬라이싱
```Python
a=[1,2,3,4,5]
b=a[:2] #처음부터 a[2] 전까지
c=a[2:] #a[2]부터 끝까지

# b=[1,2] , c=[3,4,5]
```
* 리스트의 수정 (슬라이싱와 인덱싱의 차이)
```Python
a=[1,2,3]

a[1:2] = ['a','b','c'] # index 1부터 a 리스트를 수정 => [1,'a','b','c',3]
a[1] = ['a','b','c'] # index 1을 리스트로 수정 [1,['a','b','c'],3]

a[1:3]=[] # index 1부터 3 전까지 삭제 => [1,'c',4] == del[1:3]
```
* 리스트 관련 함수
```Python
a=[1,2,3]

a.append(4) # a=[1,2,3,4]
a.append([5,6]) # a=[1,2,3,4,[5,6]]

a.sort() # 오름차순 정렬
a.reverse() # 현재 리스트를 거꾸로 정렬

a.insert(0,4) # a[0]에 4를 삽입
a.remove(3) # 리스트에 있는 정수 3를 제거(중복이라면 첫번째 나오는 요소에만 해당)
a.pop() # 리스트의 맨 마지막 요소를 반환 후 제거
a.pop(1) # a[1]의 요소를 반환 후 제거
```

### 튜플(tuple)
1. 튜플은 요소 값을 변경할 수 없다.
2. 이외에는 리스트와 동일한 특성을 가진다.

```Python
t1= (1,2,'a','b') #튜플은 소괄호로 표시한다.
t1[1:] #(2,'a','b')
```
### 딕셔너리 (dict) aka 해싱(hashing)
1. key와 value를 한 쌍으로 갖는다.
2. 순차적으로 요소값을 구하지 않고 'Key'를 통해 요소값을 구한다.
(not sequantial)
3. key값은 중복될 수 없으며 바뀔 수 없다 -> 리스트는 key값으로 쓸 수 없으나 튜플은 가능.

* 딕셔너리의 추가,삭제
```Python
a={1:'a'}

a[2]='b' 
#딕셔너리 a에 2:'b' 한 쌍을 추가 
a={2:'b',1:'a'}

del a[1]
#딕셔너리 a에 있는 key가 1인 요소를 삭제(indexing 아님)
a={2:'b'}
```
* 딕셔너리 관련 함수
```Python
a={'name':'pey','phone':'0119993323', 'birth':'1118'}

a.keys() #딕셔너리 a의 key들을 dict_keys()로 리턴
          #dict_keys(['name','phone','birth'])
list(a.keys()]  #딕셔너리 a의 키들을 리스트 자료형으로 리턴
                #['name','phone','birth']

a.values() #딕셔너리 a의 value들을 dict_values()로 리턴
a.items() #딕셔너리 a의 key,value 쌍을 튜플로 묶은 값은 dict_items()로 리턴
          #dict_items([('name','pey'),('phone','0119993323'),('birth','1118')])

a.get(x) #딕셔너리 a에 x의 value를 반환, 없으면 none을 리턴
a[x] #딕셔너리 a에 x의 value를 반환, 없으면 컴파일 오류 발생

'name' in a # 딕셔너리 a에 'name'이라는 key가 있으면 true를 리턴, 없으면 false를 리턴.
```
### 집합 (set)
1. 중복을 가지지 않고 순서가 없다 -> 딕셔너리와 같음.
2. 하지만 딕셔너리 처럼 요소값을 쌍으로 가지진 않는다.

* 집합 자료형 활용
```Python
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

s1 & s2 # 교집합, {4,5,6}

s1 | s2 # 합집합, {1,2,3,4,5,6,7,8,9}

s1 - s2 # 차집합, {1,2,3}
s2 - s1 # {8,9,7} 순서가 왜 바뀜????
```

* 집합 관련 함수
```Python
s1 = set([1,2,3])

s1.add(4) # 값 1개 추가 {1,2,3,4}

s1.update([4,5,6]) # 값 여러 개 추가 {1,2,3,4,5,6}

s1.remove(3) # 특정 값 제거 {1,2,4,5,6}
```

* 집합 자료형 변환하기
```Python
s1 = set([1,2,3])

l1 = list(s1) # 리스트로 변환, [1,2,3] 
t1 = tuple(s1) # 튜플로 변환, (1,2,3) 
```
<hr/>
2주차 마감 
  
=> 난이도가 높은 자바 스프링부트는 다음으로 미루고 파이썬과 알고리즘으로 다음 학기를 대비하는 것으로 학습 목표를 변경했다.
<hr/>

# 2022.07.24
Python 자료형 예제 정리 및 백준 단계별 풀어보기 정렬 문제 

### 수 정렬하기1 (#2750)
시간 복잡도가 O(n^2)인 알고리즘을 통해 정렬하는 문제.

시간 복잡도가 n^2이므로 이중 루프를 사용한다. 안쪽 반복문에서 이웃 요소끼리 반복 비교와 스왑으로 가장 큰 수를 찾고 가장 큰 수가 뒤로 간다고 생각하면 된다.

n의 크기가 작을 땐 (<1000?) 이 알고리즘을 써도 큰 차이는 없다.
```C
#include <stdio.h>

int main()
{
    int size,tmp=0;
    scanf("%d",&size);

    int num[size];
    for(int i=0; i<size; i++)
    {
        scanf("%d",&num[i]);
    }

    for(int i=0; i<size-1; i++) //두개씩 비교하므로 size-1까지 인덱싱
    {
        for (int j=0; j<size-1-i; j++)
        {
            if(num[j]>num[j+1]){
            tmp = num[j+1];
            num[j+1] = num[j];
            num[j] = tmp; //swap
            }
        }
        
    }

    for(int i=0; i<size; i++)
    {
        printf("%d\n",num[i]);
    }

    return 0;
}
```
### 수 정렬하기2 (#2751)
시간 복잡도가 O(nlogn)인 알고리즘으로 해결하는 문제였다.

O(n^2) 알고리즘은 버블 정렬이나 삽입 정렬로 간단하게 구현했었는데 이 경우에는 구현하기 보단 라이브러리에 있는 퀵소트를 사용했다.

stdlib.h 헤더파일에 있는 qsort 함수는 자료형에 관계 없는 함수 포인터를 사용했다. (void*)

정말 오랜만에 본 개념이라 헷갈렸다. void*로 compare 함수의 매개변수로 받고는 형 변환과 역참조를 통해 int 변수에 값을 저장한다.

```C
#include <stdio.h>
#include <stdlib.h>

int compare(const void* a,const void *b)  //const void*를 매개변수로 받는다!
{
    int num1 = *(int *)a;
    int num2 = *(int *)b; //key point, 형 변환 + 역참조
    if(num1<num2)
        return -1;
    if(num1>num2)
        return 1;
    return 0;
}

int main()
{
    int size=0;
    scanf("%d",&size);

    int num[size];
    for(int i=0; i<size; i++)
    {
        scanf("%d",&num[i]);
    }

    qsort(num,sizeof(num)/sizeof(int),sizeof(int),compare);
               //-> 크기가 정해진 int,double의 경우는 size 변수를 입력해도 되지만, 구조체를 쓰게 되는 경우를 대비해 sizeof 함수를 쓰는 것이 좋다.
    for(int i=0; i<size; i++)
    {
        printf("%d\n",num[i]);
    }
}
```
### 나이순 정렬(#10814)
stable sort는 언제 정렬해도 같은 값에 대해 똑같은 순서를 유지하는 정렬 알고리즘이다. (merge sort, bubble sort, insertion sort)

기본적으로 나이순으로 정렬하고 나이가 같다면 배열에 추가된 순서대로 정렬하는 게 조건이었다. 우선 bubble sort로 구현해봤는데 시간 초과로 실패했다.

퀵 소트는 stable sort가 아니어서 못하고 merge sort를 구현해야하는데 난이도가 높아서 일단 보류

~~빨리 파이썬을 배워야겠다~~

## Python 자료형 예제 정리
```Python
a=(1,2,3)
a=a+(4,) 
print(a)

#tuple은 리스트와 유사하나 수정할 수 없다. 함수도 2개만 있음.
#요소가 1개인 튜플을 만들 땐 쉼표를 붙인다.

a=[1,1,1,2,2,3,3,3,4,4,5]
aSet=set(a)
b=list(aSet)
print(b)

#set 자료형은 중복 요소가 없다.
#자료형을 변환 할땐 list(),tuple(),set() !!

a=['Life','is','too','short']
result=" ".join(a) 
print(result)

#join 함수를 통해 리스트를 문자열로 이동할 수 있다.
```

# 2022.07.25
Python 제어문 (if,while,for)과 입출력 학습

### 조건문 (if)
1. if 조건문을 만들 때는 "if 조건문:" 아래로 속하는 문장에 대해 들여쓰기

2. and,or,not 연산을 기호로 쓰지 않아도 됨
```python
money = 2000
card = 1
if money >= 3000 or card: #or
    print("택시를 타고 가라")
else:
    print("걸어가라")  #택시를 타고 가라
```
3. 리스트,튜플,문자열과 같은 자료형에 대한 x in s, x not in s 조건문
```python
1 in [1,2,3] #True

1 not [1,2,3] #True

'a' in ('a','b','c')

'j' not in 'python'
```
4. else if는 elif로 표현

### 반복문 (while,for)
1. while의 경우 조건문이 참인 동안 속한 문장들이 반복적으로 수행

2. for의 경우 리스트나 튜플,문자열의 첫 번째 요소부터 마지막까지 차례대로 변수에 대입되어 속한 문장들을 반복적으로 수행
```Python
a=0
while a < 10:
    a += 1
    if a % 2 ==0: continue
    print(a)

a = [(1,2),(3,4),(5,6)]
for (first,last) in a:  #리스트 a의 숫자 쌍이 first,last에 대입
    print(first + last) 
```
3. range 함수를 통해 for문에서의 범위를 설정
```python
sum = 0
for i in range(1,11): #1부터 10까지 (시작 번호는 포함, 끝 번호는 미포함)
    sum = sum + i
 
 marks = [90,25,67,45,80]
 for number in range(len(marks)): #0번 인덱스부터 4번 인덱스까지
    if marks[number] < 60: continue
    print("%d번 학생 합격입니다." % (number+1))
```
4. 리스트 안에 for문 포함하기
```python
a = [1,2,3,4]
result = [num * 3 for num in a]
print(result)
#[3,6,9,12]

result = [num * 3 for num in a if num % 2 ==0] #if 조건을 추가할 수도 있음.
print(result)
# [6,12]
```

### 프로그램의 입출력
* 함수의 입력
1. 입력값의 갯수 정해져 있을 땐 매개변수를 통해 입력 받는다.

2. 입력값의 갯수가 정해져 있지 않다면 *args를 이용한다.
```python
def sum_many(*args) #입력 변수에 *을 붙이면 입력값을 전부 모아 튜플로 만든다.
    sum = 0
    for i in args:
        sum = sum + i
    return sum
result = sum_many(1,2,3) args=(1,2,3) 튜플
print(result) #6
```
3. 입력 인수에 초깃값을 미리 설정해서 자바의 method overloading 처럼 쓸 수도 있다.
```python
def say_myself(name,old,man = True): #초깃값을 미리 설정할 입력 변수는 항상 뒤쪽에 위치시켜야 함.
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("박응용",27)
say_myself("박응용",27,True) #두 호출문 모두 똑같은 결과
```
* 사용자 입출력
1. 사용자가 입력한 값을 변수에 대입하기 위해서는 input() 함수를 사용한다.

2. input에 입력되는 모든 것은 문자열로 취급된다.

3. 출력을 하기 위해서는 print()함수를 사용한다.
  
  3-1. 큰 따옴표로 둘러싸인 문자열은 + 연산과 동일
  
  3-2. 문자열 띄어 쓰기는 콤마로 한다.
```python
print("life""is""too short") #lifeistoo short
print("life" + "is" + "too" + "short") #lifeistoo short

print("life","is","too short") #life is too short

for i in range(10):
    print(i, end=' ')
    # 0 1 2 3 4 5 6 7 8 9
```
* 파일 입출력
1. 파일 열기 모드에는 3가지가 있다.

    1-1. f = open("newfile.txt",'w'), 쓰기 모드 write, 파일을 생성 후 첫 내용을 쓸 때
    
    1-2. f = open("newfile.txt",'r'), 읽기 모드 read, 파일을 읽기만 할 때
    
    1-3. f = open("newfile.txt",'a'), 추가 모드 append, 파일의 마지막에 새로운 내용을 추가할 때
    
2. with 문을 사용하면 with 블록을 벗어나는 순간 파일 객체 f가 자동으로 close 된다.
```python
f = open("newfile.txt",'w')
for i in range(1,11):
    data = "%d line\n" % i
    f.write(data) #파일 입력 ('w)
f.close() # 열린 파일은 직접 닫는 것이 좋다.

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

```
# 2022.07.26
백준 단계별 문제 풀기 - 집합과 맵

### 숫자 카드1 (#10815)
```c
#include <stdio.h>
#include <stdlib.h>

int compare(const void* a,const void* b)
{
    int num1=*(int*)a;
    int num2=*(int*)b;

    if (num1>num2)
        return 1;
    else if (num1<num2)
        return -1;
    else if (num1==num2)
        return 0;
}

int main()
{
    int have_num; int* result;
    scanf("%d",&have_num);
    int have[have_num];
    for(int i=0; i<have_num;i++)
    {
        scanf("%d",&have[i]);
    }

    int check_num;
    scanf("%d",&check_num);
    int check[check_num];
    for(int i=0; i<check_num;i++)
    {
        scanf("%d",&check[i]);
    }

    qsort(have,sizeof(have)/sizeof(int),sizeof(int),compare);
    //binary search를 위해서는 배열이 정렬되어 있어야 한다 !
    //단순 대입(brute force)로 하면 시간 복잡도가 n^2이 된다.

    for(int i=0;i<check_num;i++)
    {
        result=(int*)bsearch(&(check[i]),have,sizeof(have)/sizeof(int),sizeof(int),compare);
        //bsearch(찾을 요소의 포인터,찾을 배열,배열의 크기,요소의 크기,compare 함수포인터)
        //bsearch 함수는 void* 형태로 요소 값이 위치한 인덱스의 포인터를 반환한다.
        if(result!=NULL)
            check[i]=1;
        else
            check[i]=0;
        
        printf("%d ",check[i]);
    }

    return 0;
}
```
처음에는 이중 for문으로 하나씩 검색했는데 시간 초과로 틀렸다.

그래서 시간 복잡도가 적은 이진 탐색을 이용했고 이진 탐색을 이용하기 위해서는 탐색해야하는 배열이 정렬되어 있어야 했다.

그래서 퀵소트 내장함수로 미리 정렬했다. 새로운 내장함수 bsearch를 이용해 볼 수 있었다.

### 문자열 집합 - C(#14425)
```c
typedef struct {
    char str[501];
} String;

    int sum=0;
    int *result; char garbage;
    qsort(string,set,sizeof(String),compare);

    for(int i=0;i<search_n;i++)
    {
        result = (int*)bsearch(search[i].str,string,set,sizeof(String),compare);
        if(result != NULL){
            *string[i].str=garbage;
            qsort(string,set,sizeof(String),compare);
            sum++;
        }
    }
    printf("%d\n",sum);
```
최대 인덱스가 500인 문자열을 구조체로 구현해서 숫자 카드 문제와 비슷하게 접근했다.

하지만 탐색 값이 중복되는 걸 방지하기 위해서 이미 탐색된 값은 garbage 값을 대입하였는데,
여기서 값이 바뀌면 다시 퀵소트로 정렬해야만 이진 탐색을 사용할 수 있었다.

이진 탐색과 퀵 소트를 반복해서 사용하다보니 시간초과로 틀렸다. 중복 문제 해결에 대해 다시 생각해봐야겠다.

### 문자열 집합 - Python (#14425)

```python
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
```
한 줄에 두 개 이상의 입력을 받기 위해 map() 함수를 이용했다, map(받을 자료형,input(출력 텍스트),split())

파이썬에는 집합 자료형과 관련 함수가 구현되어 있어 구현이 편했다.

백준에서는 index error로 런타임 에러가 발생했는데 원인을 모르겠다......

# 2022.07.27
* 문자열 집합 문제 마무리
```Python
n,m = map(int,input().split()) #한 줄에 2개 이상의 정수 받을 땐 map() 함수 이용

s1 = set()
l1 = []
for i in range(n):
    str = input()
    s1.add(str)

for j in range(m):
    str = input()
    l1.append(str)
#  s2.add(str) # 저장하면 중복을 제거하기 때문에 index error

sum = 0
for k in range(m):
    if(l1[k] in s1):
        sum = sum + 1

print(sum)
```
map() 함수로 값을 입력 받는데 그 크기가 너무 클 땐
```Python
import sys

input = sys.stdin.readline

n,m = map(int,input().split()) # or map(int,sys.stdin.readline().split())
```
# 2022.08.01 
백준 단계별 문제풀기 및 파이썬 5장 학습

### 나이순 정렬(#10814) - Python
파이썬 중첩 리스트와 람다식으로 구현해보았다. C언어로 구현할때보다 코드 길이도 짧고 편했다.

```Python
n = int(input())
l1 = []
for i in range(n):
    age,name = map(str, input().split()) #map으로 두 입력값을 str로 받기 int과 str로 받을순 없나ㅣ?
    l1.append([int(age),i,name]) # age를 int로 형변환 하지 않았더니 에러가 떴었다
l1.sort(key=lambda x: (x[0],x[1])) # 이차원 이상의 배열에서 람다식을 이용한 sort() 함수 사용 -> 각 리스트의 0번째 인덱스를 기준으로 정렬한 다음, 같은 값에 대해 1번째 인덱스로 정렬
for i in range(n):
    print("%s %s" % (l1[i][0],l1[i][2]))
```
### 파이썬과 클래스

* self, 인스턴스
```Python
class FourCal:
    #일시적으로 아무것도 안쓸 땐 pass를 쓴다.
     def setdata(self, first, second): #메소드의 첫번째 매개변수는 관례적으로 self를 사용한다.
         self.first = first #self = 어떤 객체의 이름
         self.second = second
         
a = FourCal()
a.setdata(4,2) #매개변수를 2개만 입력해도 객체 a가 자동으로 self에 입력된다.
```
![image](https://user-images.githubusercontent.com/108285793/182524490-f32890af-abb9-4220-9b35-3910b4d8ba0c.png)


* __init__, 생성자

init 메소드를 사용하면 생성자처럼 사용할 수 있다.
```python
class FourCal:
     def __init__(self, first, second): 
         self.first = first 
         self.second = second
         
a = FourCal(4,2)
a.first() # = 4
```

* 상속 , 오버라이딩
```python
 class MoreFourCal(FourCal): # 상속은 클래스 이름 뒤에 괄호를 이용한다.
     def pow(self):
         result = self.first ** self.second
         return result
         
     def div(self):      #FourCal 클래스의 div 메소드를 오버라이딩
         if self.second = 0:
            return 0
         else:
            return self.first/self.second
```

* 클래스 변수 
```python
class Family:
    lastname = "김"

a = Family()
b = Family()

a.lastname = "최"

print(a.lastname) # 최
print(b.lastname) # 김
print(Family.lastname) #김
```

# 2022.08.02

### 파이썬의 모듈, 패키지

* 모듈

모듈 : 함수나 변수, 클래스를 모아놓은 파일, 모든 .py파일

```python
# mod1.py

PI = 3.141592

class Math:
    def solv(self,r):
        return PI * (r ** 2)
def add(a, b):
    return a+b

def sub(a,b):
    return a-b
```

* 모듈 불러오기

모듈을 불러오기 위해서는 호출 파일과 피호출 파일이 같은 디렉토리에 있어야 한다.
```python
import mod1 #import 모듈이름
print(mod1.add(3,4)) #7
print(mod1.sub(4,2)) #2

from mod1 import add # 모듈 이름 없이 임의의 함수를 이름만 쓰고 싶을때
from mod1 import * # import 내의 모든 함수를 이름만 쓰고 싶을때

add(3,4) #7
sub(4,2) #2

print(mod1.PI) #3.141592

a = mod1.Math()

print(a.solv(2)) #12.566..

```
변수와 클래스 또한 사용할 수 있다

* if name == "main": 의미

mod1 모듈에 실행문이 있으면 모듈이 import 될때 마다 실행된다.

이러한 문제를 방지하기 위해 실행문을 if name == "main"안에 배치하여야 한다.

```python
# mod1.py 
def add(a, b): 
    return a+b

def sub(a, b): 
    return a-b

if __name__ == "__main__":
    print(add(1, 4))
    print(sub(4, 2))
```

* 패키지

패키지 = 파이썬 모듈을 계층적으로 관리. (디렉터리 구조)

* 패키지 생성과 실행

```python
C:/doit/game/__init__.py
C:/doit/game/sound/__init__.py
C:/doit/game/sound/echo.py
C:/doit/game/graphic/__init__.py
C:/doit/game/graphic/render.py
```

각 디렉터리에 init.py파일을 만들어만 놓기

```python
# echo.py
def echo_test():
    print("echo")
    
# render.py
def render_test():
    print("render")
    
# 패키지 안의 함수 실행 방법 첫번째
import game.sound.echo
game.sound.echo.echo.test() # echo

#두번째
from game.sound import echo 
echo.echo.test() # echo, game.sound는 생략

#세번째
from game.sound.echo import echo_test()
echo.test() #echo 파일까지 생략
```

디렉토리를 import할 때, 

1. init.py 파일에 정의되어 있지 않은 모듈이나 패키지를 호출하거나

2. import 마지막 항목을 모듈이나 패키지로 호출하지 않은 경우는

패키지 내부의 함수를 호출할 수 없다.

```python
# 안되는 경우

import game
game.sound.echo.echo_test()

#game 파일을 import하면 game 파일의 init.py에 정의한 것만 참조 할 수 있음.

import game.sound.echo.echo_test # import를 사용할 때 마지막 항목은 모듈 or 패키지여야 한다.

```

* init.py의 용도

해당 디렉토리가 패키지의 일부임을 나타내는 역할. 이 파일이 없으면 패키지로 인식되지 않는다.

```python
# C:/doit/game/sound/__init__.py
__all__ = ['echo']
```

init.py 파일 내부에는 all 변수를 선언한 뒤 import 할 수 있는 모듈들을 정의해 주어야 한다.

sound 디렉토리에서 별 표시를 이용하여 전체를 import할 경우 이곳에 정의되어 있는 echo 모듈만 import할 수 있다는 의미가 된다.

<hr/>
※ 모듈에 대해서 별 표시로 import할 경우에는 all 변수와 상관없이 모든 함수를 사용할 수 있다.
<hr/>

* relative 접근자

.. - 부모 디렉토리에 접근
. - 현재 디렉토리에 접근

```python
# render.py
from game.sound.echo import echo_test # relative하지 않게 
def render_test():
    print("render")
    echo_test()
    
# render.py
from ..sound.echo import echo_test #render.py의 부모 디렉토리인 game에 접근한 후 sound.echo로 접근하여 import

def render_test():
    print("render")
    echo_test()
```

# 2022.08.04

파이썬 예외처리 방법, 유용한 내장함수와 라이브러리, 연습문제

### 파이썬 예외처리

* try ... except

except문은 try 블럭에서 오류가 발생했을 때 오류를 처리하는 블럭이다.
```python
try:
    ...
except:
    ... # 오류의 종류와 관계없이 오류가 발생하면 예외 처리

except 발생오류(ZeroDivisionError):
    ... # zero division 오류가 발생한 경우에만 예외 처리
```
* try ... finally

finally절은 오류 발생 여부와 상관없이 항상 실행된다. 파일 리소스를 close할 때 주로 사용.
```python
f = open('foo.txt', 'w')
try:
    # 무언가를 수행한다.
finally:
    f.close()
```

여러 개의 오류를 처리할 땐 except절의 우선순위는 없음

같은 예외 처리를 위해 괄호로 묶어 나타낼 수도 있다.

```python
try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError as e:
    print(e)
except IndexError as e: #index error가 먼저 발생
    print(e)
    
try:
    a = [1,2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)
```
* try ... [except] ... else

try 블럭에서 오류가 발생하지 않을 경우에 실행되는 else문도 있다.
```python
try:
    age=int(input('나이를 입력하세요: '))
except:
    print('입력이 정확하지 않습니다.')
else:
    if age <= 18:
        print('미성년자는 출입금지입니다.')
    else:
        print('환영합니다.')
```

* 오류를 발생시키는 raise 명령어

파이썬은 raise 명령어를 사용해 오류를 강제로 발생시킬 수 있다.

```python
class Bird:
    def fly(self):
        raise NotImplementedError # 파이썬 내장함수, 함수를 구현하지 않고 일부러 오류를 발생할 때 사용한다.
        
class Eagle(Bird):
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()  #very fast
```

### 내장함수와 라이브러리

![image](https://user-images.githubusercontent.com/108285793/182750599-f2032cee-2eda-4e99-8b4f-51f661c482d9.png)
![image](https://user-images.githubusercontent.com/108285793/182750620-50381379-aa36-47e5-af39-b4ddb76da1d8.png)
* filter

![image](https://user-images.githubusercontent.com/108285793/182750772-822c8989-4f24-4ea0-bf68-176fac906251.png)
![image](https://user-images.githubusercontent.com/108285793/182750859-fabf644a-0f55-4087-9083-d48035e9828a.png)
```python
list(map(lambda a: a*2, [1, 2, 3, 4]))
# [2, 4, 6, 8] 따로 클래스를 만들지 않고도 람다식을 통해 표현할 수 있다.
```
![image](https://user-images.githubusercontent.com/108285793/182750982-069beaf6-9cb4-4725-b804-b9f502fb8a1f.png)
![image](https://user-images.githubusercontent.com/108285793/182751049-98ec0b85-7d63-4d7a-8b77-19ab11e91913.png)


# 2022.08.06
파이썬 교재 6장 연습문제

### 문자열 압축하기
```python
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
```

### Duplicated Numbers
```python
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
```

### 모스 부호 해독
```python
str = input().split('  ') #공백 2개를 기준으로 인덱스 나누기
for i in range(len(str)):
    str[i]=list(str[i].split(' ')) #공백 1개를 기준으로 중첩 문자열 내부의 인덱스 구분으로 문자를 1개씩 분리
for i in range(len(str)):
    for j in range(len(str[i])):  #이중 중첩문과 조건문으로 리스트 내부를 알파벳으로 바꾸기
        if str[i][j] == '.-':
            str[i][j] = 'A'
        elif str[i][j] == '-...':
            str[i][j] = 'B'  # A,B ~ Z
        print('%c' % str[i][j], end = '') #줄이 바뀌지 않도록 end = ' '를 추가해준다
    print('', end = ' ')
```

# 2022.08.07
7장 파이썬 정규 표현식과 XML

정규 표현식이란? -> 복잡한 문자열을 처리할 때 사용하는 기법.

### 메타 문자

* 문자 클래스 []

정규 표현식이 [abc]라면 a,b,c 중 한개의 문자와 매치를 뜻한다. ( ex. [abc]와 before은 b가 매치, [abc]와 dude는 매치 하지 않음)

대괄호 안에 하이픈(-)을 사용하면 범위를 나타낸다. [0-5] = [012345] , [a-zA-z] = 알파벳 전체 , [0-9] = 숫자 전체

(^) 메타 문자가 사용되면 반대의 의미를 갖게 된다. [^0-9] = 숫자가 아닌 문자

* Dot(.)

줄바꿈 문자를 제외한 a와 b 사이의 문자가 모든 문자와 매치

```python
# 정규식이 a.b일때..
aab # a 문자가 매치
a0b # 0 문자가 매치
abc # a와 b 사이에 아무 문자도 없으므로 매치 X
```

* 반복(*,+,{m,n},?)

별 표시 바로 앞의 문자가 0번 이상부터 무한대로 반복되면 매치 

더하기 표시 바로 앞의 문자가 1번 이상부터 무한대로 반복되면 매치

{m,n}으로 반복횟수를 제한할 수도 있다 (3회 반복될때만 매치로 판정하고 싶은 경우)

(ex. ca{2}t = a가 2번만 반복되면 매치 ca{2,5}t = a가 2번~5번 반복되면 매치)

물음표 표시는 {m,n}으로 표시하면 {0,1}, 별 표시와 더하기 표시의 교집합이다.

# 2022.08.09
백준 단계별 문제 풀이 (그리디 알고리즘, 스택)

### 동전 0 (#11047)
```python
n,k = map(int, input().split())
coin = []
for i in range(n):
    type = input()
    coin.append(int(type))
coin.reverse()
count = 0
for j in range(n):
    while coin[j] <= k:
        count +=  k // coin[j]  #빼기로 하면 틀린다!!
        k %= coin[j]
print(count) 
```

### 스택 (#10828)

```python
n = int(input())
l1 = []
result = []
for i in range(n):
    do = input()
    c = do.split(' ')[0]
    if c == 'push':
        l1.append(do.split(' ')[1])
    elif c == 'pop':
        try:
            result.append(l1.pop())
        except:
            result.append('-1')
    elif c == 'size':
        result.append(len(l1))
    elif c == 'empty':
        if len(l1) == 0:
            result.append('1')
        else:
            result.append('0')
    elif c == 'top':
        try:
            result.append(l1[len(l1)-1])
        except:
            result.append('-1')
for j in range(len(result)):
    print(result[j])
```

# 2022.08.11 
백준 단계별 문제풀이 큐(Queue)

### 큐2 (#18258)
```python
import sys
from collections import deque 

n = int(sys.stdin.readline()) #input()으로 받는것보다 빠르고 많은 양을 받을 수 있다.
l1 = deque([]) 
for i in range(n):
    do = sys.stdin.readline().split() #split()은 시간복잡도에 큰 영향을 끼치진 않는듯?
    if do[0] == 'push':
        l1.append(do[1]) #append() = O(1)
    elif do[0] == 'pop':
        if not l1:
            print('-1')
        else:
            print(l1.popleft()) #deque로 선언하면 맨 왼쪽요소를 pop할수 있음 = O(1)
                                #일반 리스트로 선언하여 pop(0)을 하게 되면 나머지 인덱스 요소를 앞으로 붙여야하므로
                                #시간 복잡도가 O(n)이 된다.
    elif do[0] == 'size':
        print(len(l1)) 
    elif do[0] == 'empty':
        if len(l1) == 0: 
            print('1')
        else:
            print('0')
    elif do[0] == 'front':
        try:
            print(l1[0]) #배열로의 접근 = O(1)
        except:
            print('-1')
    elif do[0] == 'back':
        try:
            print(l1[len(l1)-1])
        except:
            print('-1')
```

# 2022.08.13
백준 단계별 문제풀기 이진탐색

### 수 찾기 (#1920)
```python
n = int(input())
num_set = set(map(int,input().split()))
m = int(input())
check = list(map(int,input().split()))

for i in range(m):
    if check[i] in num_set:
        check[i] = 1
    else:
        check[i] = 0
    print(check[i])
```

https://velog.io/@ready2start/Python-%EC%84%B8%ED%8A%B8set%EC%9D%98-%EC%8B%9C%EA%B0%84-%EB%B3%B5%EC%9E%A1%EB%8F%84

이진탐색을 사용하진 않았지만 파이썬에선 집합이라는 자료형으로 O(1)의 탐색이 가능하다!

하지만 집합은 중복되는 수를 입력할 수 없기 때문에 한계가 있음 (숫자카드 2 문제 참고)
