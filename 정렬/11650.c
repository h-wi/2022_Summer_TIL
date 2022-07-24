#include <stdio.h>
#include <stdlib.h>

typedef struct dict {
    int x;
    int y;
} dic;

int compare(const void *a,const void *b)
{
    dic c1 =*(dic*)a;  //*(type*)a
    dic c2 =*(dic*)b; //*(type*)b 형 변환 + 역참조

    if(c1.x > c2.x)
        return 1;

    if(c1.x < c2.x)
        return -1;

    if(c1.x == c2.x)
    {
        if(c1.y>c2.y)
            return 1;
        else   
            return -1;
    }

}

int main()
{
    int n;
    scanf("%d",&n);
    
    dic dict[n];

    for (int i=0; i<n; i++)
    {
        scanf("%d %d",&dict[i].x,&dict[i].y);
    }
    
    qsort(dict,sizeof(dict)/sizeof(dic),sizeof(dic),compare); //퀵소트 O(logn*n)
                                                    //sizeof(dict)/sizeof(dic) 중요!!

    for(int i=0; i<n; i++)
    {
        printf("%d %d\n",dict[i].x,dict[i].y);
    }
    return 0;
}

   // for(int i=0; i<n-1; i++)
    // {
    //     for(int j=0; j<n-1-i; j++)
    //     {
    //         if(dict[j].x>dict[j+1].x)
    //         {
    //             tmp = dict[j+1];
    //             dict[j+1] = dict[j];
    //             dict[j] = tmp;
    //         }
    //         else if (dict[j].x == dict[j+1].x)
    //         {
    //             if(dict[j].y > dict[j+1].y)
    //             {
    //                 tmp = dict[j+1];
    //                 dict[j+1] = dict[j];
    //                 dict[j] = tmp;
    //             }
    //         }
    //     }
    // } bubble sort -> 시간 초과