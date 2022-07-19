#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main()
{
    char n[7];
    scanf("%s",n);

    int sum=0; int tmp;
    int len=strlen(n);
    int min=__INT_MAX__;

    for(int i=0;i<(int)pow(10,len);i++)
    {
        sum += i;
        tmp=i;
        while(tmp!=0)
        {
            sum += tmp%10;
            tmp = tmp/10;
        }
        if (sum==atoi(n)&&sum<min)
            min = i;
        sum = 0;
    }
    if(min==__INT_MAX__)
        printf("0\n");
    else        
        printf("%d\n",min);
    return 0;
}