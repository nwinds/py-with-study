
/* reference： http://mosir.org/html/y2012/the-custom-start-address-of-c-program.html
 * TODO use standard format
 */
#include <stdio.h>

#include <stdlib.h>
int myentry(int argc, char *argv[])
{
    printf("Start from myentry\n");
    /*
     * return 0;// this is made as default 'clean up for main'
     */
    exit(0);
}
