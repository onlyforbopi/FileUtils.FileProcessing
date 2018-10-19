#!/usr/bin/gawk -f

# NOTE: string 1st char at col. 1.

# Functions.
function process_4recs_invoice(rc1, rc2, rc3, rc4){
   PREPAID_POS = 875
   PREPAID_LEN = 1
   PREPAID_VAL = "1"
   flag_prepaid = ""
   
   flag_prepaid = substr(rc4, PREPAID_POS, PREPAID_LEN)
   
   # If prepaid.
   if (flag_prepaid == PREPAID_VAL)
   {
      print rc1 >> FILE_OT
      print rc2 >> FILE_OT
      print rc3 >> FILE_OT
      print rc4 >> FILE_OT
      line_cnt_ot += 4
   }
}

# Before first line.
BEGIN {
   print ""             >> JOB_OUT
   print "GAwk Started" >> JOB_OUT

   # Constants.
   NUM_RECS_INVC = 4

   # Variables Init.
   line_crnt= ""
   #
   line_cnt_in = 0
   line_cnt_ot = 0
   #
   modulo = 69
   #
   rec1 = ""
   rec2 = ""
   rec3 = ""
   rec4 = ""
}

# For each line of input.
{ 
   line_cnt_in += 1
   line_crnt = $0
   
   modulo = line_cnt_in % NUM_RECS_INVC
   switch (modulo){
      case 0:
         rec4 = line_crnt
         process_4recs_invoice(rec1, rec2, rec3, rec4)
         break
      case 1:
         rec1 = line_crnt
         break
      case 2:
         rec2 = line_crnt
         break
      case 3:
         rec3 = line_crnt
         break
      default:
         print "line_cnt_in % NUM_RECS_INVC = " (line_cnt_in % NUM_RECS_INVC) >> JOB_OUT
         exit
         break
   }
}

# After last line.
END {
   print ""           >> JOB_OUT
   print "Read : line_cnt_in = @" line_cnt_in "@" >> JOB_OUT
   print "Writ : line_cnt_ot = @" line_cnt_ot "@" >> JOB_OUT
   print ""           >> JOB_OUT
   print "GAwk Ended" >> JOB_OUT
}
