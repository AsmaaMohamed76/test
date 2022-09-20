#include<stdio.h>
#include<stdlib.h>
int main()
    {
      char color[20];
      char pluralNoun[20];
      char celebrityf[20];
      char celebrityl[20];  

      printf("Enter a Color: ");
      scanf("%s", color);
      printf("Enter a Plural Noun: ");
      scanf("%s", pluralNoun);
      printf("Enter a Celebrity : ");
      scanf("%s %s", celebrityf ,celebrityl);
      printf("Rose are %s\n", color);
      printf("%s are blue \n",pluralNoun);
      printf("I Love %s %s\n", celebrityf ,celebrityl);
      return 0;

    }
