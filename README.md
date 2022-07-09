# TIL
* Python 학습서 : 박응용, 점프 투 파이썬(2019)
* Springboot 학습서 : 이동욱, 스프링 부트와 AWS로 혼자 구현하는 웹 서비스(2019)

백준 코딩테스트 학습(C,Python) 및 백엔드 스터디
# 2022.07.09
계획 
1. VScode 및 InteliJ 설치 및 개발 환경 설정 
2. 코딩테스트 학습 계획 수립
* VScode C언어 구동환경 설정
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

* 코딩테스트 학습 계획 수립

매주 모임마다 각 팀원별로 일주일동안 공부한 문제 리뷰 

Python 학습은 시간적 여유가 있을 때 하기로 결정함.
(계절학기나 백엔드 구현 학습량에 대한 부담)

C언어로 코딩테스트로 변경, 기존 파이썬을 학습한 조원은 파이썬으로 그대로 진행.
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
