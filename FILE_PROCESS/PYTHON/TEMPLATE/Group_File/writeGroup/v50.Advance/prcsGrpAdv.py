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

HEADER_KEY     = "1"
DETAIL_KEY     = "3"
MASTER_KEY     = "5"
FOOTER_KEY     = "9"

# Variables.
ftr_cnt        = 0
ftr_sum        = 0

grp_cnt        = 0
grp_sum        = 0

line_in        = ""
line_pv        = ""

cur_key        = ""
prv_key        = ""

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
      
      get_keys()
      
      print("line_in =", line_in) # Debug
      print("line_pv =", line_pv) # Debug
      print("cur_key =", cur_key, "prv_key =", prv_key) # Debug.
      
      # If first line.
      if fcnt_in == 1 :
         print("fcnt_in =", fcnt_in, "first line") # Debug
         if cur_key != HEADER_KEY :
            print("ERROR at 1st line: cur_key != HEADER_KEY", cur_key, HEADER_KEY)
            sys.exit(69)         
         
         fp_ot.write(line_in)
         init_group()
         line_pv = line_in # Previous = Current.
         continue

      # If header line.
      if cur_key == HEADER_KEY :
         print("fcnt_in =", fcnt_in, "first line") # Debug
         
         write_footer(fp_ot)
         fp_ot.write(line_in)
         init_group()
      # If detail line.
      elif cur_key == DETAIL_KEY :
         prcs_wrt_line(line_in, fp_ot) # Process and write current line.
      # If master line.
      elif cur_key == MASTER_KEY :
         chk_wrt_master(line_in, fp_ot)
      else :
         print("ERROR: Invalid cur_key =", cur_key)
         sys.exit(66)
      
      line_pv = line_in # Previous = Current.
   # for end.
   
   # (At EOF) Write last footer.
   write_footer(fp_ot)
   
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
   
   return 0;
# get_keys end.

def            init_group() :
   global      grp_cnt, grp_sum
   global      ftr_cnt, ftr_sum
   
   grp_cnt = 0
   grp_sum = 0
   ftr_cnt = 0
   ftr_sum = 0
   
   return 0
# init_group end.

def            prcs_wrt_line(line, fp) :
   global      grp_cnt, grp_sum
   
   fp.write(line)
   grp_cnt += 1
   
   line_amnt_int = int(line[1:4])   
   grp_sum += line_amnt_int
   
   return 0
# prcs_wrt_line end.

def            chk_wrt_master(line, fp) :
   "Documentation."
   global      ftr_cnt, ftr_sum
   global      grp_cnt, grp_sum
   
   v_grp_cnt = int(line[1:4])
   v_grp_sum = int(line[4:9])
   
   ftr_cnt += v_grp_cnt
   ftr_sum += v_grp_sum
   
   fp.write(line)
# chk_wrt_master end.

def            write_footer(fp) :
   global      ftr_cnt, ftr_sum
   
   line_ot = FOOTER_KEY + '{:03d}{:05d}'.format(ftr_cnt, ftr_sum) + '\n'
   fp.write(line_ot)
# write_footer end.

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

