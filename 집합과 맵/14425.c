#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char str[501];
} String;

int compare(const void* a,const void* b)
{
    String str1 = *(String *)a;
    String str2 = *(String *)b;

    if(strcmp(str1.str,str2.str)==1)
        return 1;
    else if(strcmp(str1.str,str2.str)==-1)
        return -1;
    else
        return 0;
}

int main()
{
    int set,search_n;
    scanf("%d %d",&set,&search_n);
    String string[set],search[search_n];

    for(int i=0;i<set;i++)
        scanf("%s",string[i].str);
    for(int i=0;i<search_n;i++){
        scanf("%s",search[i].str);
    }

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
    return 0;
}