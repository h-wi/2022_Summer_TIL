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

    for(int i=0; i<size-1; i++)
    {
        for (int j=0; j<size-1-i; j++)
        {
            if(num[j]>num[j+1]){
            tmp = num[j+1];
            num[j+1] = num[j];
            num[j] = tmp;
            }
        }
        
    }

    for(int i=0; i<size; i++)
    {
        printf("%d\n",num[i]);
    }

    return 0;
}