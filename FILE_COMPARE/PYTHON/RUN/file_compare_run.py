#!/usr/bin/python

###############################################################################
# Packages.
import sys

###############################################################################
# Global variables.

fltrName = ""
baseName = ""
comnName = ""
diffName = ""

fltrStrt = -1
fltrLeng = -1
baseStrt = -1
baseLeng = -1

# Constants.
ARG_NUM = 6

###############################################################################
# Functions.

def chk_args( p_sys_argv ):
   "Check command-line arguments."
   
   global ARG_NUM
   global fltrName, baseName, comnName, diffName
   global fltrStrt, fltrLeng, baseStrt, baseLeng
   
   if len(p_sys_argv) - 1 != ARG_NUM :
      print "WRONG number of arguments: ", len(p_sys_argv) - 1
      print "Must be: ", ARG_NUM
      print "Usage:", sys.argv[0], " File_Filter", "File_Base", " Filter_Start", "Filter_Length", " Base_Start", "Base_Length"
      return 0
   else :
      fltrName = sys.argv[1]
      baseName = sys.argv[2]
      comnName = baseName + ".cmn"
      diffName = baseName + ".dif"
      
      fltrStrt = int(sys.argv[3], 10)
      fltrLeng = int(sys.argv[4], 10)
      baseStrt = int(sys.argv[5], 10)
      baseLeng = int(sys.argv[6], 10)

      return 1

###############################################################################
# Start.

print sys.argv[0], "Started." ; print

# Check arguments.
print "Checking arguments..."

if chk_args( sys.argv ) == 0 :
   print "Exiting..."
   sys.exit(69)

print "fltrName = ", fltrName
print "baseName = ", baseName
print "comnName = ", comnName
print "diffName = ", diffName
print "fltrStrt = ", fltrStrt
print "fltrLeng = ", fltrLeng
print "baseStrt = ", baseStrt
print "baseLeng = ", baseLeng

###############################################################################
# Load fltr file to table.

print; print "Loading filter file to table..."

fltrFile = open(fltrName, "r")
fltrList = []

fltrFrom = fltrStrt - 1
fltrTo   = fltrFrom + fltrLeng

for fltrLine in fltrFile :
   fltrIndx = fltrLine[fltrFrom : fltrTo]
   fltrList.append(fltrIndx)
   # print(fltrIndx)

fltrFile.close()

###############################################################################
# Proces base file.

print; print "Processing base file..."

baseFile = open(baseName, "r")
comnFile = open(comnName, "w")
diffFile = open(diffName, "w")

baseFrom = baseStrt - 1
baseTo   = baseFrom + baseLeng

for baseLine in baseFile:
   baseIndx = baseLine[baseFrom : baseTo]
   # print(baseIndx)
   
   if baseIndx in fltrList :
      comnFile.write(baseLine)
   else :
      diffFile.write(baseLine)

baseFile.close()
comnFile.close()
diffFile.close()

###############################################################################
# End.

print; print sys.argv[0], "Ended."
