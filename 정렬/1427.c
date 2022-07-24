#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char num[10];
    int array[10]; int tmp;

    scanf("%s",num);

    for(int i=0; i<strlen(num); i++)
    {
        array[i] = num[i]-'0';
    }

    for(int i=0; i<strlen(num)-1; i++)
    {
        for(int j=0; j<strlen(num)-1-i; j++)
        {
            if (array[j]<array[j+1]) {
                tmp = array[j+1];
                array[j+1] = array[j];
                array[j] = tmp;
            }
        }
    }

    for(int i=0; i<strlen(num); i++)
    {
        num[i] = array[i]+'0';
    }

    printf("%d\n",atoi(num));
    
    return 0;
}