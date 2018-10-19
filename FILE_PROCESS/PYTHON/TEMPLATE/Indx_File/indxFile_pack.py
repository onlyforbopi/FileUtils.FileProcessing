###############################################################################
# Packages.
# System.
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
      print "ERROR in number of arguments: ", len(p_sys_argv) - 1
      print "Must be: ", ARG_NUM
      print "Usage:", sys.argv[0], " File_Filter", "File_Inpt"
      return 0
   else :
      fltrName = sys.argv[1]
      fileName = sys.argv[2]
      out1Name = fileName + ".ot"
      return 1
#

def load_file2table(p_fltrDict, p_fltrCntr):
   "load file to table."
   
   global fltrName

   print "\nLoading filter file to dictionary..."

   fltrFile = open(fltrName, "r")

   for fltrLine in fltrFile :
      p_fltrCntr += 1
      fltrKey = fltrLine[0:11]
      fltrVal = fltrLine
      p_fltrDict[fltrKey] = fltrVal

   fltrFile.close()
   
   print "Ended"
#

def procs_inp_file(fltrDict, fileCntr):
   "Process input file."
      
   global fileName, out1Name
   
   print; print "Processing input file..."

   fileFile = open(fileName, "r")
   out1File = open(out1Name, "w")

   for fileLine in fileFile:
      
      fileCntr += 1
      fileIndx  = fileLine[0:11]
      
      if fileIndx in fltrDict :
         out1Line = fileLine
                    # '\n'
         out1File.write(out1Line)
      else :
         print "NOT FOUND: fileCntr =", str(fileCntr), " fileIndx =", fileIndx

   fileFile.close()
   out1File.close()

   print "Ended."
#
