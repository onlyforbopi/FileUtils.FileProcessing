# -*- coding: utf-8 -*-

###############################################################################
# Packages.

import sys, os, operator # System.
import pyPrcsFile_pack # User.

###############################################################################
# Start.
print; print sys.argv[0], "Started."; print

# Check arguments.
print "Checking arguments..."
rtrnVal = pyPrcsFile_pack.chk_args( sys.argv )

if rtrnVal == 0 :
   print "Exiting..."
   # sys.exit(69)
   sys.exit(rtrnVal + 69)

print "fil1Name = ", pyPrcsFile_pack.fil1Name
print "out1Name = ", pyPrcsFile_pack.out1Name
#

###############################################################################
# Proces input file.

print; print "Processing input file..."

fil1File = open(pyPrcsFile_pack.fil1Name, "r")
out1File = open(pyPrcsFile_pack.out1Name, "w")

fil1Cntr = 0

for fil1Line in fil1File:   
   fil1Cntr += 1
   pyPrcsFile_pack.process_rec(fil1Cntr, fil1Line, out1File)

print("Read : ", str(fil1Cntr), "lines.")
print("Write: ", str(pyPrcsFile_pack.fil2Cntr), "lines.")
#

###############################################################################
# End.

fil1File.close()
out1File.close()

print; print sys.argv[0], "Ended."; print
#
