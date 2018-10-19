# -*- coding: utf-8 -*-

###############################################################################
# Packages.

import sys, os, operator # System.

###############################################################################
# Global variables.

fil1Name = ""
out1Name = ""
fil2Cntr = 0

# Constants.
ARG_NUM = 1
#

###############################################################################
# Functions.

def chk_args( p_sys_argv ):
   "Check command-line arguments."
   
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

def process_rec(p_fil1Cntr, p_fil1Line, p_out1File):
   "process_rec."
   
   global fil2Cntr
   
   if ' ' in p_fil1Line :
      p_out1File.write(p_fil1Line)
      fil2Cntr += 1
   
   return 0
#
