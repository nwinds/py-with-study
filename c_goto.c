/* gotoaddr.c */
#include <stdio.h>
#include <time.h>
int main(int argc,char *argv[])
{
	void *target[] = {&&eventag, &&oddtag};
    int id;
	time_t now;
	now = time((time_t *)NULL);
	goto *target[now%2];
eventag:
	printf("The time value %ld is even\n",now);
	return(0);
oddtag:
	printf("The time value %ld is odd\n",now);
	return(0);
}

