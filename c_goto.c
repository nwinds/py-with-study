/* gotoaddr.c */
#include <stdio.h>
#include <time.h>
int main(int argc,char *argv[])
{
	void *target;
	time_t now;
	now = time((time_t *)NULL);
	if(now & 0x0001)
		target = &&oddtag;
	else
		target = &&eventag;
	goto *target;
eventag:
	printf("The time value %ld is even/n",now);
	return(0);
oddtag:
	printf("The time value %ld is odd/n",now);
	return(0);
}

