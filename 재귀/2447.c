#include <stdio.h>

void stars(int n)
{
    int i,j=1;
    for(i=1;i<=n;i++)
    {
        for(j=1;j<=n;j++)
        {
            if(i>(n/3)&&i<=n-(n/3)&&
                 j>(n/3)&&j<=n-(n/3))
            {
                printf(" ");
                continue;
            }
            if(n==3)
                printf("*");
            else 
                stars(n/3);
        }
        printf("\n");
    }
}

int main()
{
    int n=0;
    scanf("%d",&n);
    stars(n);
    return 0;
}

/*
동적 배열 할당으로 다시 만들어보기
3x3을 이어붙이기는 불가능한듯.
*********         *********
* ** ** *         * ** ** *
*********         *********
***   ***         ***   ***
* *   * *         * *   * *
***   ***         ***   ***
*********         *********
* ** ** *         * ** ** *
*********         *********

*/