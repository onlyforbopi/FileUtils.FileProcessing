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
KEY_LENGTH     = 2
TYP_START      = 4
TYP_LENGTH     = 1
MSTR_TYP       = "0"
TRAN_TYP       = "1"

# Variables.
fil1Name       = ""
out1Name       = ""
line_in        = ""
line_pv        = ""
cur_key        = ""
prv_key        = ""
cur_typ        = ""
prv_typ        = ""

###############################################################################
# Functions.

def            main() :
   global      line_in, line_pv, \
               cur_key, prv_key, \
               cur_typ, prv_type
   global      FNAME_IN, FNAME_OT
   
   print("Main started.\n")
   
   fp_in = open_file(FNAME_IN, "r")
   fp_ot = open_file(FNAME_OT, "w")
   
   fcnt_in = 0
   hollow_read = False
   # Foreach line of input file.
   for line_in in fp_in :
      fcnt_in += 1
      
      print("fcnt_in =", fcnt_in) # Debug
      
      if hollow_read :
         line_pv = line_in # Previous = Current.
         hollow_read = False
         continue
            
      get_keys_types(fcnt_in)
      
      print("line_in =", line_in) # Debug
      print("line_pv =", line_pv) # Debug
      print("cur_key =", cur_key, "prv_key =", prv_key) # Debug.
      print("cur_typ =", cur_typ, "prv_typ =", prv_typ) # Debug.
      
      # If first line.
      if fcnt_in == 1 :
         print("first line") # Debug
         line_pv = line_in # Previous = Current.
         continue;
      
      # If current = master.
      if cur_typ == MSTR_TYP :
         print("Master.") # Debug.
         
         # Write previous line.
         fp_ot.write(line_pv[0:4] + '\n')
         line_pv = line_in # Previous = Current.
         continue;
      
      # If current = trans.
      if cur_typ == TRAN_TYP :
         print("Trans.") # Debug.
         
         # If previous = trans.
         if prv_typ == TRAN_TYP :
            print("Prev-Trans.") # Debug.
            # Write previous line.
            fp_ot.write(line_pv[0:4] + '\n')
         # Else previous = master.
         else :
            print("Prev-Master.") # Debug.
            # If same key.
            if cur_key == prv_key :
               print("Same keys.") # Debug.
               upd_wrt_mstr(fp_ot)
               hollow_read = True
            # Else different key.
            else :
               # Write previous line.
               print("Diff keys.") # Debug.
               fp_ot.write(line_pv[0:4] + '\n')

         line_pv = line_in # Previous = Current.
         continue;
      # if end.
   # for end.
   
   # (At EOF) Process last line.
   # # If current = master.
   # if cur_typ == MSTR_TYP :
      # print("End Master.") # Debug.
      
      # # Write previous line.
      # fp_ot.write(line_pv[0:4] + '\n')
   # # If current = trans.
   # elif cur_typ == TRAN_TYP :
      # print("End Trans.") # Debug.
      
      # # If previous = trans.
      # if prv_typ == TRAN_TYP :
         # print("Prev-Trans.") # Debug.
         # # Write previous line.
         # fp_ot.write(line_pv[0:4] + '\n')
      # # Else previous = master.
      # else :
         # print("Prev-Master.") # Debug.
         # # If same key.
         # if cur_key == prv_key :
            # print("Same keys.") # Debug.
            # upd_wrt_mstr(fp_ot)
            # hollow_read = True
         # # Else different key.
         # else :
            # # Write previous line.
            # print("Diff keys.") # Debug.
            # fp_ot.write(line_pv[0:4] + '\n')
   
   if not hollow_read :
      fp_ot.write(line_in[0:4] + '\n')

   fp_in.close()
   fp_ot.close()
   
   print("Main ended.\n");   
   return 0
# Main end.

def            get_keys_types(cnt) :
   global      cur_key, prv_key
   global      cur_typ, prv_type
   global      line_in, line_pv
   
   print("get_keys_types() line_in =", line_in, "line_pv =", line_pv) # Debug.
   
   cur_key = line_in[KEY_START : KEY_START + KEY_LENGTH]
   prv_key = line_pv[KEY_START : KEY_START + KEY_LENGTH]
 
   print("get_keys_types() cur_key =", cur_key, "prv_key =", prv_key) # Debug.
   
   cur_typ = line_in[TYP_START : TYP_START + TYP_LENGTH]
   prv_typ = line_pv[TYP_START : TYP_START + TYP_LENGTH]
   
   print("get_keys_types() cur_typ =", cur_typ, "prv_typ =", prv_typ) # Debug.
   
   if (cur_typ != MSTR_TYP) and \
      (cur_typ != TRAN_TYP) :
      print("ERROR: Illegal cur_typ =", cur_typ, "!=", MSTR_TYP, TRAN_TYP)
      sys.exit(69)

   if cnt != 1 :
      if (prv_typ != MSTR_TYP) and (prv_typ != TRAN_TYP) :
         print("ERROR: Illegal prv_typ =", prv_typ, "!=", MSTR_TYP, TRAN_TYP)
         sys.exit(68)

   return 0;
# get_keys_types end.

def            upd_wrt_mstr(fp) :
   "Documentation."
   global      line_in, line_pv, prv_key
   
   # Current = tran, Previous = master, same keys.
   
   line_in_cnt = int(line_in[2:4])
   line_pv_cnt = int(line_pv[2:4])
   sum_cnt = line_in_cnt + line_pv_cnt
   line_ot = prv_key + '{:02d}'.format(sum_cnt) + '\n'
   fp.write(line_ot)
   
   return 0;
# upd_wrt_mstr end.

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

