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

# 2022.07.18
Python 학습 및 백준 단계별 풀이 (재귀)

## Python의 자료형과 문자열 포매팅
* Python에서의 새로운 연산
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

* 문자열 관련 함수

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
동적 할당으로 배열을 만들고 이중 for문으로 출력하는 게 나을 듯.

