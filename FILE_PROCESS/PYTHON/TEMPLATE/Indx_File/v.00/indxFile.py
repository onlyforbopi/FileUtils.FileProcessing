#!/usr/bin/python

# Load index file1 to table, process file2.

###############################################################################
# Packages.
import sys

###############################################################################
# Global variables.

fltrName = ""
fileName = ""
out1Name = ""

# Constants.
ARG_NUM = 2

###############################################################################
# Functions.
def chk_args( p_sys_argv ):
   "Check command-line arguments."
   
   global ARG_NUM
   global fltrName, fileName, out1Name
   
   if len(p_sys_argv) - 1 != ARG_NUM :
      print "WRONG number of arguments: ", len(p_sys_argv) - 1
      print "Must be: ", ARG_NUM
      print "Usage:", sys.argv[0], " File_Filter", "File_Inpt"
      return 0
   else :
      fltrName = sys.argv[1]
      fileName = sys.argv[2]
      out1Name = fileName + ".ot"
      return 1
#

###############################################################################
# Main.

print sys.argv[0], "Started." ; print

# Check arguments.
print "Checking arguments..."

if chk_args( sys.argv ) == 0 :
   print "Exiting..."
   sys.exit(69)

print "fltrName = ", fltrName
print "fileName = ", fileName
print "out1Name = ", out1Name
#

###############################################################################
# Load filter file to dictionary.

print; print "Loading filter file to dictionary..."

fltrFile = open(fltrName, "r")
fltrDict = {}
fltrCntr = 0

for fltrLine in fltrFile :
   fltrCntr += 1
   fltrKey = fltrLine[0:44] + fltrLine[49:]
   fltrVal = fltrLine
   fltrDict[fltrKey] = fltrVal

fltrFile.close()
#

###############################################################################
# Proces input file.

print; print "Processing input file..."

fileFile = open(fileName, "r")
out1File = open(out1Name, "w")

fileCntr = 0

for fileLine in fileFile:
   
   fileCntr += 1
   fileIndx  = fileLine[4001:]
   
   if fileIndx in fltrDict :
      out1Line = fileLine[0:4045] + \
                 fltrDict[fileIndx][44:49] + \
                 fileLine[4045:]
                 # '\n'
      out1File.write(out1Line)
   else :
      print "??? NOT FOUND:"
      print "??? fileCntr =", str(fileCntr), " fileIndx =", fileIndx
      print "??? exiting..."
      sys.exit(68)

fileFile.close()
out1File.close()

print; print sys.argv[0], "Ended."
#
