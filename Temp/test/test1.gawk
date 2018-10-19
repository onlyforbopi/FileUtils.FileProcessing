# # gawk vs. nawk

# Before first line.
BEGIN {
   print "Awk Started"
   FILE_OT_YHAV="FILE_OT_YHAV.test"
   FILE_OT_NHAV="FILE_OT_NHAV.test"
   #FS=" +"
}

# For each line of input.
{ 
   fline=$0
   print fline
   print length(fline)
   
   # if ( (substr($0,112,7) != "0000000") || (substr($0,123,7) != "0000000") )
      # print $0 > FILE_OT_YHAV;
   # else
      # print $0 > FILE_OT_NHAV;
	
}

# After last line.
END {
   print "Awk Ended"
}
