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

    for(int i=0; i<size; i++)
    {
        printf("%d\n",num[i]);
    }
}