// CS495-20 Homework 3
# include <stdio.h>
# include <stdlib.h>
# include <string.h>


//static PyObject* rank_order(PyObject *self, PyObject *args)
int rank_order(int argc, char **argv)
{

	char* nums = argv[1];
	int occurrences[10];
	int i, j, num;
	for (i=0; i<10; i++)
		occurrences[i] = 0;		
	for (num=0; num<10; num++)
	{
		for (i=0; i<strlen(nums); i++)
		{
			if (nums[i] == num)
				occurrences[num]++;
		}
	}
	
	int pairs[10];
	int tempswap;
	for (i=0; i<10; i++)
	{
		for(j=i; j<10; j++)
		{
			if (pairs[i] < pairs[j])
			{
				tempswap = pairs[j];
				pairs[j] = pairs[i];
				pairs[i] = tempswap;
			}
		}
	}
	
	int currcnt = 0;
	int countvalue = pairs[0];
	for(i=0; i<10; i++)
	{
		if (countvalue != pairs[i])
		{
			currcnt++;
			countvalue = pairs[i];
		}
	}
	int rank_counts[currcnt];

	countvalue = pairs[0];
	for(i=0; i<currcnt; i++)
		rank_counts[i] = 0;
	currcnt = 0;
	for(i=0; i<10; i++)
	{
		if (countvalue != pairs[i])
		{
			rank_counts[currcnt]++;
			currcnt++;
			countvalue = pairs[i];
		}
	}
	
	printf("{");
	for(i=0; i<currcnt; i++)
		printf("%d: %d,", i, rank_counts);
	printf("}");
	return 1;
}	
