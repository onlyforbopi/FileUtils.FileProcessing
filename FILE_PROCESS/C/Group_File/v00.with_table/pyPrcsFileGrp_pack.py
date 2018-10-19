###############################################################################
# Packages.

import sys, os, operator # System.

###############################################################################
# Global variables.

fil1Name = ""
out1Name = ""

# Constants.
ARG_NUM = 1
#

###############################################################################
# Functions.

def chk_args( p_sys_argv ):
   "Check command-line arguments."
   
   global ARG_NUM
   global fil1Name, out1Name
   
   argsLen = len(p_sys_argv)
   
   if argsLen - 1 == ARG_NUM :
      fil1Name = sys.argv[1]
      out1Name = fil1Name + ".ot"
      return 1
   elif argsLen - 2 == ARG_NUM :
      fil1Name = sys.argv[1]
      out1Name = sys.argv[2]
      return 2
   else :
      print "WRONG number of arguments: ", argsLen - 1
      print "Must be: ", ARG_NUM, " or ", ARG_NUM + 1
      print "Usage:", sys.argv[0], "File_Input [File_Output]"
      return 0
#

def write_rec(p_fil1Cntr, p_fil1Line, p_out1File):
   "Write record."
   
   vfil1Cntr = '%05d' % (p_fil1Cntr)
   
   # outpLine = p_fil1Line[0:44] + \
              # vfil1Cntr + \
              # p_fil1Line[44:]
              # # '\n'
   outpLine = p_fil1Line
   p_out1File.write(outpLine)
   
   return 0
#
