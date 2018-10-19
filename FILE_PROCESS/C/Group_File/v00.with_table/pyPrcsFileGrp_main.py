#!/usr/bin/python

###############################################################################
# Packages.

import sys, os, operator # System.
import pyPrcsFileGrp_pack # User.

###############################################################################
# Start.
print; print sys.argv[0], "Started."; print

# Check arguments.
print "Checking arguments..."
rtrnVal = pyPrcsFileGrp_pack.chk_args( sys.argv )

if rtrnVal == 0 :
   print "Exiting..."
   # sys.exit(69)
   sys.exit(rtrnVal + 69)

print "fil1Name = ", pyPrcsFileGrp_pack.fil1Name
print "out1Name = ", pyPrcsFileGrp_pack.out1Name
#

###############################################################################
# Proces input file.

print; print "Processing input file..."

fil1File = open(pyPrcsFileGrp_pack.fil1Name, "r")
out1File = open(pyPrcsFileGrp_pack.out1Name, "w")

fil1Cntr = 0
# fil1PrevKey = ""

for fil1Line in fil1File :
   fil1Cntr += 1

   # If first input line.
   if fil1Cntr == 1 :
      # Init group.
      pyPrcsFileGrp_pack.grpCnt = 0
      pyPrcsFileGrp_pack.grpSum = 0
      fil1CrntLst = fil1Line.split(";")
      fil1CrntKey = fil1CrntLst[0]
      fil1PrevKey = fil1CrntKey
      # Process line.
      pyPrcsFileGrp_pack.grpCnt += 1 
      pyPrcsFileGrp_pack.grpSum += int(fil1CrntLst[0])
   # if end.
   
   fil1CrntLst = fil1Line.split(";")
   fil1CrntKey = fil1CrntLst[0]
   
   # If different group.
   if fil1CrntKey != fil1PrevKey :
      fil1Cntr = 1
   
   pyPrcsFileGrp_pack.write_rec(fil1Cntr, fil1Line, out1File)
   fil1PrevKey = fil1CrntKey
#

###############################################################################
# End.

fil1File.close()
out1File.close()

print; print sys.argv[0], "Ended."; print
#
