#!/usr/bin/python

###############################################################################
# Packages.

import sys, os, operator # System.
import pyPrcsLoga_pack # User.

###############################################################################
# Start.
print; print sys.argv[0], "Started."; print

# Check arguments.
print "Checking arguments..."

if pyPrcsLoga_pack.chk_args( sys.argv ) == 0 :
   print "Exiting..."
   sys.exit(69)

print "fil1Name = ", pyPrcsLoga_pack.fil1Name
print "out1Name = ", pyPrcsLoga_pack.out1Name
#

###############################################################################
# Proces input file (4 recs per invoice).

print; print "Processing input file..."

fil1File = open(pyPrcsLoga_pack.fil1Name, "r")
out1File = open(pyPrcsLoga_pack.out1Name, "w")

fil2Cntr = 0

for fil1Line in fil1File:
   
   fil2Cntr += 1
   
   if   fil2Cntr % 4 == 1 :
      fil1Line1 = fil1Line
      continue
   elif fil2Cntr % 4 == 2 :
      fil1Line2 = fil1Line
      continue
   elif fil2Cntr % 4 == 3 :
      fil1Line3 = fil1Line
      continue
   elif fil2Cntr % 4 == 0 :
      fil1Line4 = fil1Line
      pyPrcsLoga_pack.process_4recs(fil1Line1, fil1Line2, fil1Line3, fil1Line4, out1File)
   else :
      print "??? WHAT: fil2Cntr % 4 = " + str(fil2Cntr % 4) + " ???"
      sys.exit(68)
#

###############################################################################
# End.

fil1File.close()
out1File.close()

print; print sys.argv[0], "Ended."; print
#
