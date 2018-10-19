#include    <stdio.h>
#include    <stdlib.h>
#include    <string.h>

#define     FNAME_IN       "test.in"
#define     FNAME_OT       "test.ot"
#define     MAXLINE        1024
#define     MAXGRUP        65536

char        line_in[MAXLINE],
            line_pv[MAXLINE],
            cur_key[MAXLINE],
            prv_key[MAXLINE],
            line_tb[MAXGRUP][MAXLINE];
int         grp_cnt = 0,
            grp_sum = 0;

FILE*       open_file(char *fname, char mode[]);
int         write_group(FILE *fp);
int         write_file(char *line, FILE *fp);
int         init_group();
int         prcs_wrt_line(char *line, FILE *fp);

int         main()
{
   FILE     *fp_in, *fp_ot;
   
   int      fcnt_in;
   
   printf("Main started.\n");
   
   fp_in = open_file(FNAME_IN, "r");
   fp_ot = open_file(FNAME_OT, "w");
   
   fcnt_in = 0;
   while (fgets(line_in, sizeof(line_in), fp_in) != NULL)
   {
      fcnt_in++;
      
      // If first line.
      if (fcnt_in == 1)
      {
         init_group();
         prcs_wrt_line(line_in, fp_ot);
         continue;
      }
      
      get_keys();
      
      // If different group.
      if (strcmp(cur_key, prv_key) != 0)
      {
         write_group(fp_ot);
         init_group();
      }
      
      // Process and write current line.
      prcs_wrt_line(line_in, fp_ot);
      // Previous = Current.
      strcpy(line_pv, line_in);
   } // while end.
   
   // (At EOF) Write last group.
   write_group(fp_ot);
   
   fclose(fp_in);
   fclose(fp_ot);
   
   printf("Main ended.\n");   
   return 0;
}

int         get_keys()
{
   memcpy(cur_key, &line_in[0], 1);
   cur_key[1] = '\0';

   memcpy(prv_key, &line_pv[0], 1);
   prv_key[1] = '\0';
   
   return 0;
}

int         init_group()
{
   grp_cnt = 0;
   grp_sum = 0;
   strcpy(line_pv, line_in);
   get_keys();
   
   return 0;
}

int         write_group(FILE *fp)
{
   char     int_to_str[32];
   
   sprintf(int_to_str, "%03d%05d\n", grp_cnt, grp_sum);
   write_file(int_to_str, fp);
   
   return 0;
}

int         prcs_wrt_line(char *line, FILE *fp)
{
   char     line_amnt_str[32];
   int      line_amnt_int;
   
   write_file(line, fp);
   grp_cnt++;
   
   memset(line_amnt_str, '\0', sizeof(line_amnt_str));
   strncpy(line_amnt_str, line + 1, 3);
   line_amnt_int = atoi(line_amnt_str);
   
   grp_sum += line_amnt_int;
   
   return 0;
}

FILE*       open_file(char fname[], char mode[])
{
   FILE     *fp;
   
   fp = fopen(fname, mode);
   
   if (fp == NULL)
   {
      printf("ERROR: Cannot open file @%s@ with mode @%s@.\n", fname, mode);
      exit(99);
   }
   else
      return fp;
} // open_file end.

int         write_file(char *line, FILE *fp)
{
   if (fputs(line, fp) == EOF)
   {
      printf("ERROR: Cannot write line @%s@ to file.\n", line);
      exit(98);
   }
   
   return 0;
} // write_file end.
