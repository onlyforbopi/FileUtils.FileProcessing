#!/usr/bin/gawk -f

# NOTE: string 1st char at col. 1.

# Before first line.
BEGIN {
   print ""             >> JOB_OUT
   print "GAwk Started" >> JOB_OUT

   # Constants.
   CNST_DAYS_THLD= 480

   # Variables Init.
   line_crnt= ""
   line_writ= ""
   #
   line_cnt_in= 0
   line_cnt_ot= 0
   #
   in_sum_days_litr_ftox= 0
   #
   ot_acct= ""
   ot_sum_days_litr_ftox= ""
   ot_offc= ""
   ot_offc_regn= ""
   ot_offc_cust= ""
   ot_muncp_code= ""
}

# For each line of input.
{ 
   line_cnt_in+= 1
   
   line_crnt= $0
   in_sum_days_litr_ftox= substr(line_crnt, 69, 3)
      
   if (in_sum_days_litr_ftox >= CNST_DAYS_THLD)
   {  
      ot_acct= substr(line_crnt, 2, 11)
      ot_sum_days_litr_ftox= in_sum_days_litr_ftox
      ot_offc_regn= substr(line_crnt, 2, 1)
      ot_offc_cust= substr(line_crnt, 13, 2)
      ot_offc= ot_offc_regn ot_offc_cust
      ot_muncp_code= substr(line_crnt, 179, 4)
      #
      line_writ= ot_acct ot_sum_days_litr_ftox ot_offc ot_muncp_code
      print line_writ >> FILE_OT
      line_cnt_ot+=1
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
