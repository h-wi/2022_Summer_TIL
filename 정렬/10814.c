#include <stdio.h>
/*stable sort *언제 정렬해도 같은 값에 대해 똑같은 순서 유지
  -> merge sort, insertion sort, bubble sort */
typedef struct {
    int age;
    int index;
    char name[100];
} inform;

int main()
{
    int n; inform tmp;
    scanf("%d",&n);
    inform inf[n]; 
    for(int i=0;i<n;i++)
    {
        scanf("%d %s",&inf[i].age,inf[i].name);
        inf[i].index=i;
    }

    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n-1-i;j++)
        {
            if(inf[j].age>inf[j+1].age){
                tmp = inf[j+1];
                inf[j+1] = inf[j];
                inf[j] = tmp;
            }
            else if (inf[j].age==inf[j+1].age)
            {
                if(inf[j].index>inf[j+1].index){
                tmp = inf[j+1];
                inf[j+1] = inf[j];
                inf[j] = tmp;
            }
            }
        }
    } //bubble sort 시간초과, 무조건 merge sort..? 시간 줄이는 다른 방법은?

    for(int i=0;i<n;i++)
    {
        printf("%d %s\n",inf[i].age,inf[i].name);
    }
    return 0;
}