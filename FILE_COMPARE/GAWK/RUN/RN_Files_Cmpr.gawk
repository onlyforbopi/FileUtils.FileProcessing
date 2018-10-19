#!/usr/bin/gawk -f

# Note: strings' 1st character is at column 1.

#################################################################################################
#                                                                                                                                                                                                                                                                                           ##
#  Job:           RUN_Files_Cmpr.gawk
#  Location:      /home/tede/n55115/Joblib/Utils/file_processing/FILE_COMPARE/GAWK/RUN
#  
#  Description:   Find differences / common between two files based on specified substrings
#  
#  Called by:     RUN.RN_Files_Cmpr.gawk.bsh <FILE_IN_fltr> <FILE_IN_BASE> <fltr_LINE_START> <fltr_LINE_LENGTH> <BASE_LINE_START> <BASE_LINE_LENGTH>RUN.TM_Prcs_Files_in_Dir  <dir>  <rcrs>
#  Parameters:    FILE_OT_COMN		( Common Lines )
#                 FILE_OT_DIFF    	( Differing Lines )
#                 JOB_OUT			( Run log files )
#                 p_fltr_srt		( <fltr_LINE_START> above )
#                 p_fltr_len		( <fltr_LINE_LENGTH> above )
#                 p_base_srt		( <BASE_LINE_START> above )	
#                 p_base_len		( <BASE_LINE_LENGTH> )
#
#                 
#
#  Uses globals:  None
#
#################################################################################################
#
#  Function: (Note: doc_ functions just for documentation, not real code)
#
#  {
#	
#     #  Initialize variables			  
#		
#     #  STEP0001:
#        #  Load filter file substring into hash
#        filterhash = doc_load_filter_into_hash()
#
#        # Read Base File line by line
#		 doc_read_base_file_line_by_line()	
#		 doc_check_if_substring_exists()	
#		 	
#        # Process file_out.
#        doc_call_end_process()
#           
#        end
#  }
#  ______________________________________________________________________________________________
#
#  doc_load_filter_into_hash()
#  {
#    Iterate over filter file,
#    extract specified substring,
#	 keep counter,
#	 store substring into assoc.array. 
#  }
#  ______________________________________________________________________________________________
#
#  doc_check_if_substring_exists()
#  {
#	  #Check if substring exists in <filterhash> and output into common or diff
#     file_out_common = lines with substring present in filterhash.
#     file_out_diffs = lines with substring not present in filter hash
#	}
#  ______________________________________________________________________________________________
#
#  doc_call_end_process()
#  {
#     Report on parameters used by script
#     Report on line countsWrite file_out.
#  }
#
#################################################################################################
#
#  Output: Output files in directory <dir>.
#
#################################################################################################


# Before first line.
# BEGIN block is always executed before the file is read
BEGIN {
   print "" >> JOB_OUT
   print "GAwk Started" >> JOB_OUT

   print "p_fltr_srt = '" p_fltr_srt "'" >> JOB_OUT
   print "p_fltr_len = '" p_fltr_len "'" >> JOB_OUT
   print "p_base_srt = '" p_base_srt "'" >> JOB_OUT
   print "p_base_len = '" p_base_len "'" >> JOB_OUT
   
   # Variables Init.
   line_crnt = ""
   line_writ = ""
   #
   load_fltr = ""
   srch_fltr = ""
   #
   line_cnt_fltr = 0
   line_cnt_base = 0
   line_cnt_comn = 0
   line_cnt_diff = 0
   # We will use array:
   # tbl_filter
   
}

# For each line of input.

# 1st File (filter).
# Load filter to table.
FNR==NR {
   # Iterate over lines of file, store substring into tbl_filter hash
   # Note : Using FNR==NR in case we have 2 files, will read the lines of the first file provided.
   # Awk keeps a combined count on FNR, so when it doesnt apply anymore, it ll start raeding the second file provided.
   
   line_cnt_fltr += 1
   line_crnt = $0
   # Extract key substring 
   load_fltr = substr(line_crnt, p_fltr_srt, p_fltr_len)
   # print "fLTR '" line_cnt_fltr "'" >> JOB_OUT
   # print line_crnt >> JOB_OUT
   # print "'" load_fltr "'" >> JOB_OUT
         
   # Load key to table.
   # load_fltr=line_crnt
   tbl_filter[load_fltr] += 1
   
   next
}

# 2nd File (base).
# Read base, check filter, write output.
# Note : Here, FNR==NR does not apply, as FNR will continue incrementing after first file read - reading over the second file.
{
   line_cnt_base += 1
   line_crnt = $0
   
   # Extract key substring
   srch_fltr = substr(line_crnt, p_base_srt, p_base_len)
   # print "bASE '" line_cnt_base "'" >> JOB_OUT
   # print line_crnt >> JOB_OUT
   # print "'" srch_fltr "'" >> JOB_OUT
         
   line_writ= line_crnt
   
   # Search the tbl_filter hash for the value of srch_fltr
   # Awk uses the syntax "var in hash" that returns boolean T/F
   if (srch_fltr in tbl_filter)
   {
      # If a match was found in tbl_filter output to common file
      print line_writ >> FILE_OT_COMN
      line_cnt_comn+= 1
   }
   else
   {
      # Output to the diffs file
      print line_writ >> FILE_OT_DIFF
      line_cnt_diff+= 1
   }
}

# After last line.
# END : Code nested under the END block will be executed after any file manipulation is done.
END {
   print "" >> JOB_OUT
   print "Read : line_cnt_fltr = @" line_cnt_fltr "@" >> JOB_OUT
   print "Read : line_cnt_base = @" line_cnt_base "@" >> JOB_OUT
   print "Same : line_cnt_comn = @" line_cnt_comn "@" >> JOB_OUT
   print "Diff : line_cnt_diff = @" line_cnt_diff "@" >> JOB_OUT
   print "" >> JOB_OUT
   print "GAwk Ended" >> JOB_OUT
}
