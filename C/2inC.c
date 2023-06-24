// fibonacci Numbers? sum of the 2 previous number
// 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

#include <stdlib.h>
#include <stdio.h>

int main()
{
	
	int	first_term = 1, second_term = 2, sum = 0, temp = 0, x;
	
	printf("Enter your border: ");
	scanf("%d",&x);
	
	while(second_term<x)
	{
		if(second_term%2==0)
		{
			sum+=second_term;
		}
		
		temp = second_term;
		second_term = first_term + second_term;
		first_term = temp;
		
		temp = 0;
	}
	
	printf("sum: %d",sum);
		
}
