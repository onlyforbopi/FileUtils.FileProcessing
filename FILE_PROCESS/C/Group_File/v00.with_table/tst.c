#include    <stdio.h>
#include    <stdlib.h>
#include    <string.h>

#define     MAXLINE        1024
#define     MAXGRUP        65536

char        line_in[MAXLINE] = "asd",
            line_pv[MAXLINE],
            cur_key[MAXLINE],
            prv_key[MAXLINE],
            line_tb[MAXGRUP][MAXLINE];

int main()
{
   printf("%s\n", line_in);
   strcpy(line_tb[0], "qwe");
   printf("%s\n", line_tb[0]);
   
   return 0;
}