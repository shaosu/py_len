#include "my_fun.h"

unsigned long long fact( unsigned long long n)
{
  	if (n<=1)
		return 1;
	else
		return n*fact(n-1);
}

 
