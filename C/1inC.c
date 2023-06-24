// If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6 and 9. The sum of the muliples is 23.
// Find the sum of all the multiples of 3 or 5 below 1000.

#include <stdlib.h>
#include <stdio.h>

int main()
{
	int i,x,counter=0;
		
	printf("Enter your border number: ");
	scanf("%d",&x);
	
	for(i=0;i<x;i++)
		{

			if(i%5==0 || i%3==0)
			{
				counter=counter+i;
			}
		}	
	printf("Sum = %d",counter);
	
	return(0);
	
}
