#!/usr/bin/python

# USAGE:
# Load index file1 to table, process file2.

###############################################################################
# Packages.
# System.
import sys
import datetime
# User.
import indxFile_pack


###############################################################################
# Start.

print datetime.datetime.now()
print sys.argv[0], "Started.\n"

# Check arguments.
print "Checking arguments..."

if indxFile_pack.chk_args( sys.argv ) == 0 :
   print "Exiting..."
   sys.exit(69)

print "fltrName = ", indxFile_pack.fltrName
print "fileName = ", indxFile_pack.fileName
print "out1Name = ", indxFile_pack.out1Name
#

###############################################################################
# Load filter file to dictionary.

fltrDict = {}
fltrCntr = 0
indxFile_pack.load_file2table(fltrDict, fltrCntr)
#

###############################################################################
# Proces input file.

fileCntr = 0
indxFile_pack.procs_inp_file(fltrDict, fileCntr)
#

###############################################################################
# Start.

print "\n", datetime.datetime.now()
print sys.argv[0], "Ended."
#
