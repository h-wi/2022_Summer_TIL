#include <stdio.h>

int main()
{
    int len,n=0;
    scanf("%d %d",&len,&n);
    int cards[len];
    for(int i=0;i<len;i++)
    {
        scanf("%d",&cards[i]);
    }

    int max=0;
    int sum=0;
    for(int i=0;i<len-2;i++)
    {
        for(int j=i+1;j<len-1;j++)
        {
            for(int k=j+1;k<len;k++)
            {
                sum=cards[i]+cards[j]+cards[k];
                if(sum>max && sum<=n)
                    max = sum;
            }
        }
    }
    printf("%d\n",max);
    return 0;
}