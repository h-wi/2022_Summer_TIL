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