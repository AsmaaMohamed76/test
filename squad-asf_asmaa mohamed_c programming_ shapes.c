#include <stdio.h>
#include <stdlib.h>
#include <math.h>
//for store shapes'height
struct shapes    
{
    int height; 
};
//function to draw circle
int circle(int n)
{
    int col,row;
        printf("Enter Number of Diameter from 3 to 5 :  ");
        scanf("%d" , &n);
        printf("==========================================\n");
        if((n<=5) && (n>=3))
        
        for(row = 1; row <= n;  row++)
        {
            for(col = 1; col <= n; col++)
            {
                if((row == 1 && row != col && col != n) || (row == n && row != col && col != 1) || (col == 1 && row != n && col != row) || (col == n && row != 1 && row != n))
                {
                    printf("* ");
                }
                else
                {
                    printf("  ");
                } 
            }
            printf("\n");
          } 
        else if(n<=2 || n>5)
        {
           printf("Try Again \n");
           printf("==========================================\n");
           return circle(n);
        }
        printf("==========================================\n");
}
//function to draw pyramid
     int pyramid(int rows)
     {
        int i, j;
        char shape[rows+1];
        printf("Enter Number of Heights from 2 to 5 : ");
        scanf("%d", &rows);
          printf("==========================================\n");
        if( (rows<=5) && (rows>=2) )
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
            
        else if(rows<=1 || rows>5)
        {
            printf("Try Again \n");
            return pyramid(rows);
        }
          printf("==========================================\n");
     }
//function to draw square
    int square(int n)
    {
        printf("Enter Number of Heights from 2 to 5 : ");  
        scanf("%d",&n); 
          printf("==========================================\n");
        if((n<=5) && (n>=2))
        for(int i=0;i<n;i++) 
        {
            for(int j=0;j<n;j++) 
             {
                 printf("*"); 
             } 
              printf("\n");
        }  
        else if(n<2 || n>5)
        {
           printf("Try Again \n");
           printf("==========================================\n");
           return square(n);
        }
          printf("==========================================\n");
    } 
//function to draw right triangle
        int rightTriangle(int n)
        {
            printf("Enter Number of Heights from 3 to 5 : ");
            scanf("%d", &n);
            printf("==========================================\n");
            if((n<=5) && (n>=3))

            for(int i=1; i<=n; i++)
            {
                
                for(int j=1; j<=i; j++)
                {
                    printf("*");
                }
                printf("\n");
            }
            else if(n<2 || n>5)
            {
                printf("Try Again \n");
                printf("==========================================\n");
                return rightTriangle(n);
            }
              printf("==========================================\n");

        }

     
        
int main()
{
    while(1){
    struct shapes shape;
    char s;
    printf("1.Draw Circle\n2.Draw Pyramid\n3.Draw Square\n4.Draw Right Triangle\n5.Exit\n");
    printf("Enter The Number Of The Shape You Want : ");
    scanf("%c",&s);
        

    switch (s)
    {
        case '1':
        circle(shape.height);
        break;
    case '2':
        pyramid(shape.height);
        break;
    case '3':
        square(shape.height);
        break;
    case '4':
        rightTriangle(shape.height);
        break;
    case '5':
        exit(0);
        break;
    default:
        printf("Invaild Error\n");
        break;
    }   
    }
}

