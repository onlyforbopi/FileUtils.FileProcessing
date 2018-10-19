#!/usr/bin/python

###############################################################################
# Packages.

import sys, os, operator # System.
import pyGrpFile_pack # User.

###############################################################################
# Start.
print; print sys.argv[0], "Started."; print

# Check arguments.
print "Checking arguments..."
rtrnVal = pyGrpFile_pack.chk_args( sys.argv )

if rtrnVal == 0 :
   print "Exiting..."
   # sys.exit(69)
   sys.exit(rtrnVal + 69)

print "fil1Name = ", pyGrpFile_pack.fil1Name
print "out1Name = ", pyGrpFile_pack.out1Name
#

###############################################################################
# Proces input file.

print; print "Processing input file..."

fil1File = open(pyGrpFile_pack.fil1Name, "r")

fil1Cntr = 0
out1NmAA = 0
out1NmTp = ""
fil1LnPr = "" # Line Prev.

for fil1Line in fil1File:   
   fil1Cntr += 1
   # pyGrpFile_pack.process_rec(fil1Cntr, fil1Line)
   
   # If first input line.
   if fil1Cntr == 1 :
      out1NmAA += 1
      out1NmTp = pyGrpFile_pack.out1Name + str(out1NmAA)
      out1File = open(out1NmTp, "w")
      # out1File.write(fil1Line)
      pyGrpFile_pack.write_rec(fil1Line, out1File)
      
      fil1LnPr = fil1Line
      continue
      
   # Now we have: fil1LnPr, fil1Line
   fld1LnPv = fil1LnPr.split(";")[0]
   fld1Line = fil1Line.split(";")[0]
   
   # If same group.
   if fld1Line == fld1LnPv :
      # out1File.write(fil1Line)
      pyGrpFile_pack.write_rec(fil1Line, out1File)
      
      fil1LnPr = fil1Line
      continue
   
   # If group changed.
   if fld1Line != fld1LnPv :
      out1File.close()
      out1NmAA += 1
      out1NmTp = pyGrpFile_pack.out1Name + str(out1NmAA)
      out1File = open(out1NmTp, "w")
      # out1File.write(fil1Line)
      pyGrpFile_pack.write_rec(fil1Line, out1File)
      
      fil1LnPr = fil1Line
      continue
   
# for end.

###############################################################################
# End.

fil1File.close()
out1File.close()

print; print sys.argv[0], "Ended."; print
#
