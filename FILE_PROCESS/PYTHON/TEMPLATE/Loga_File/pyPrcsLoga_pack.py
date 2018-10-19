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
   
   if len(p_sys_argv) - 1 != ARG_NUM :
      print "WRONG number of arguments: ", len(p_sys_argv) - 1
      print "Must be: ", ARG_NUM
      print "Usage:", sys.argv[0], " File_Loga"
      return 0
   else :
      fil1Name = sys.argv[1]
      out1Name = fil1Name + ".loga"
      return 1
#

def process_4recs(p_fil1Line1, p_fil1Line2, p_fil1Line3, p_fil1Line4, p_out1File):
   "process_4recs."
   
   outpLine = p_fil1Line1.replace('\n', "") + \
              p_fil1Line2.replace('\n', "") + \
              p_fil1Line3.replace('\n', "") + \
              p_fil1Line4.replace('\n', "")
              # + '\n'
   p_out1File.write(outpLine)
   
   return 0
#
