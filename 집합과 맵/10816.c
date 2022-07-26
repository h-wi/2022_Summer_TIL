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
    
    int count=0;
    for(int i=0;i<check_num;i++)
    {
        while(1)
        {
        result=(int*)bsearch(&(check[i]),have,sizeof(have)/sizeof(int),
                            sizeof(int),compare);
        if(result==NULL)
            break;
        *result=0;
        count++;
        qsort(have,sizeof(have)/sizeof(int),sizeof(int),compare);
        }
        //tlqkf
        check[i]=count;
        printf("%d ",check[i]);
        count=0;
    }

    return 0;
}