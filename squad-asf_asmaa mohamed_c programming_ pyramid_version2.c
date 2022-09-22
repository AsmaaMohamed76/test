#include <stdio.h>

int pyramid(int rows)
{
     int i, j;
    char shape[rows+1];
     while (1)
  {
    printf("Enter Number of Rows from 2 to 5 : ");
    scanf("%d", &rows);
      if( (rows<=5) & (rows>=2) )
    for(i=1; i<=rows; i++)
    { 
        for(j=i; j<rows; j++)
        {
            printf(" ");
            shape[rows+1+1]=' ';
        }

        for(j=1; j<=(2*i-1); j++)
        {
            printf("*");
            shape[rows+1+1]='*';
        }
        printf("\n");
    }
          
      else if(rows<=0)
      {
        printf("Try Again \n");
        return pyramid(rows);
      }
    }
}


int main()
{
 
      int rows;
      pyramid( rows);
    return 0;
}
