###############################################################################
# Packages.

import sys, os, operator # System.

###############################################################################
# Globals.

# Constants.
ARG_NUM        = 0
FNAME_IN       = "test.in"
FNAME_OT       = "test.ot"
KEY_START      = 0
KEY_LENGTH     = 1
grp_cnt        = 0
grp_sum        = 0
#

# Variables.
line_in        = ""
line_pv        = ""
cur_key        = ""
prv_key        = ""
line_tb        = list()

###############################################################################
# Functions.

def            main() :
   global      line_in, line_pv
   global      cur_key, prv_key
   global      FNAME_IN, FNAME_OT
      
   print("Main started.\n")
   
   fp_in = open_file(FNAME_IN, "r")
   fp_ot = open_file(FNAME_OT, "w")
   
   fcnt_in = 0
   # Foreach line of input file.
   for line_in in fp_in :
      fcnt_in += 1
      
      print("fcnt_in =", fcnt_in) # Debug
      print("line_in =", line_in) # Debug
      
      # If first line.
      if fcnt_in == 1 :
         print("fcnt_in =", fcnt_in, "first line") # Debug
         
         init_group()
         prcs_line(line_in, fp_ot)
         continue;
      
      get_keys()
      
      print("line_in =", line_in) # Debug
      print("line_pv =", line_pv) # Debug
      print("cur_key =", cur_key, "prv_key =", prv_key) # Debug.
      
      # If different group.
      if cur_key != prv_key :
         print("Diff group.")
         write_group(fp_ot)
         init_group()
      
      prcs_line(line_in, fp_ot) # Process current line.
      line_pv = line_in # Previous = Current.
   # for end.
   
   # (At EOF) Write last group.
   write_group(fp_ot);
   
   fp_in.close()
   fp_ot.close()
   
   print("Main ended.\n");   
   return 0
# Main end.

def            get_keys() :
   global      cur_key, prv_key
   global      line_in, line_pv
   
   print("get_keys() line_in =", line_in, "line_pv =", line_pv) # Debug.
   
   cur_key = line_in[KEY_START:KEY_START+KEY_LENGTH]
   prv_key = line_pv[KEY_START:KEY_START+KEY_LENGTH]
   
   print("get_keys() cur_key =", cur_key, "prv_key =", prv_key) # Debug.

   # cur_key = line_in[0:1]
   # prv_key = line_pv[0:1]
   
   print("get_keys() cur_key =", cur_key, "prv_key =", prv_key) # Debug.

   
   return 0;
# get_keys end.

def            init_group() :
   global      grp_cnt, grp_sum
   global      line_pv, line_in, line_tb
   
   grp_cnt = 0
   grp_sum = 0
   line_tb = list()
   line_pv = line_in
   get_keys()
   
   return 0
# init_group end.

def            write_group(fp) :   
   global      grp_cnt, grp_sum
   
   for line in line_tb :
      fp.write(line)
   
   int_to_str = '{:03d}{:05d}'.format(grp_cnt, grp_sum) + '\n'
   fp.write(int_to_str)
   
   return 0
# write_group end.

def            prcs_line(line, fp) :
   global      grp_cnt, grp_sum
   global      line_tb
   
   print("grp_cnt =", grp_cnt)
   line_tb.insert(grp_cnt, line)
   grp_cnt += 1
   
   line_amnt_int = int(line[1:4])   
   grp_sum += line_amnt_int
   
   return 0
# prcs_line end.

def            open_file(fname, mode) :
   fp = open(fname, mode)
   return fp;
# open_file end.

###############################################################################
# Start.
print; print sys.argv[0], "Started."; print

main()

###############################################################################
# End.
print; print sys.argv[0], "Ended."; print

