/* THIS IS A FILE
* GENERATED BY ESCRIPT,
* DO NOT MODIFY.
*/

/* STDLIB */
#include <assert.h>
#include <errno.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

/* ESCRIPT.LIB */
#include <escript.h>

DO {
printf("Starting loop...\n");
int i = 0;
do {
    printf("%d\n", i + 1);
} while (++i < 10);
printf("Loop ended!\n");

return 0;
}