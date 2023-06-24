// The prime factors of 13195 are 5, 7, 13 and 29.
// What is the largest prime factor of the number 600851475143 ? (i would rather to take variable from user.)

#include <stdio.h>
#include <stdlib.h>

int main()
{
	long int x,i,j,largest;
	
	printf("Enter your number for largest prime factor: ");
	scanf("%d",&x);
	
	for(i=1;i<x;i++)
	{
		int primeCheck = 1;
		
		
		if(x % i == 0)
		{
			for(j=2;j<i;j++)
			{
				if(i%j==0)
				{
					primeCheck = 0;
					break;
				}
			
			}
			
			if(primeCheck)
			{
				largest = i;
			}
		}
				
	}
	
printf("%d",largest);
	
return(0);
	
}
