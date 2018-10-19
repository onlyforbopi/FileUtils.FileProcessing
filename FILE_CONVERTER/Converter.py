#!/usr/bin/python

#################################################################################################
#                                                                                                                                                                                                                                                                                           ##
#  Job: Converter.py
#  Location: /home/tede/n55115/Joblib/Utils/file_processing/FILE_CONVERTER/
#  
#  Called by: RUN.Converter.bsh <dir|file> <hex|oct>
#  Parameters: <dir> : Input directory.
#              <rcrs>: Flag for recursive process or not.
#                      Valid values: r or n respectively.
#
#  Uses global variables: RCRS_YES="r"
#                         RCRS_NOT="n"
#
#################################################################################################
#
#  Function: (Note: doc_ functions just for documentation, not real code)
#
#  {
#     #  Check for supplied parameters.
#     chk_args()
#
#     #  STEP0001:
#           #  Create line list to be processed.
#           file_list = doc_create_file_list()
#       
#           # Create output name
#           outname = doc_create_file_out_name()
#   
#           # Read line from input file and convert
#           doc_process_line(line)
#
#           # Output processed line to output file         
#  }
#  ______________________________________________________________________________________________
#
#  doc_create_file_list()
#  {
#     Create file list for directory <dir>,
#     recursively or not based on <rcrs>.
#  }
#  ______________________________________________________________________________________________
#
#  doc_create_file_out_name()
#  {
#     Create file_out name by adding a prefix or/and suffix to file_in name,
#     without full path.
#  }
#  ______________________________________________________________________________________________
#
#  doc_process_file(file_out)
#  {
#     Apply command, program or job on file_in.
#     Iterate over characters in line, get ordinal value, then convert.
#     Write file_out.
#  }
#
#################################################################################################
#
#  Output: Output files in directory <dir>.
#
#################################################################################################

import sys
import time


def tohex(string1):
    '''
    Function : Converts a string to hex
    Called as : tohex(string1)
    Notes : Translates everything including special characters, newlines
    '''
    strout = ''
    for i in string1:
        strout += str(hex(ord(i)))
    return strout
    #print (strout)
    
def tooct(string1):
    '''
    Function : Converts a string to oct
    Called as : tohex(string1)
    Notes : Translates everything including special characters, newlines
    '''
    strout = ''
    for i in string1:
        strout += str(oct(ord(i)))
    return strout
    #print (strout)
    
def chck_args_num(var):
    '''
    Function : Checks n. of variables
    Called as : chk_args(len(sys.argv))
    '''
    args_correct = 3
    args_in = var
    args_in_fixed = args_in - 1
    if args_in_fixed != args_correct:
        print ('Wrong number of arguments : ' + str(args_in_fixed))
        print ('Must be : ' + str(args_correct))
        return False
    else:
        print ('Correct number of arguments provided: ' + str(args_in_fixed) + "\n" )
        return True

        
def chck_args_type(string):
    '''
    Function : Checks the content of parameters
    Called as chck_args_type(sys.argv)
    '''
    for i in range(len(string)):
        if i == 0:
            print "Function name: %s" % sys.argv[0]
        else:
            print "%d. argument: %s" % (i,sys.argv[i])
    
    print ("\n")
    return 0
        
def script_params(filename):
    '''
    Function: Prints all the basic script parameters
    Called as: script_params(sys.argv[0])
    Notes: Always returns true
    '''
    print ('Script name : ' + filename)
    print ('Script directory : ' + sys.path[0] )
    print ('Script started at: ' + time.strftime("%c"))
    #print (sys.path)
    print ('Processing')

    
# Initialize vars    
line_out = ''
counter1 = 0
counter2 = 0


# Parse arguments
print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv), "\n"

# Check n. of arguments or terminate
if not chck_args_num(len(sys.argv)):
    print ('Terminating Script....')
    sys.exit()

chck_args_type(sys.argv)    
    
# Assign parameters    
file_name = sys.argv[1]
outp_name = sys.argv[2]
mode = sys.argv[3]

# Basic script parameters - Script Start
script_params(sys.argv[0])

# Open input file and output file
with open(file_name) as f1:
    with open(outp_name, 'a') as f2:
        # read f1 line by line
        lines = f1.readlines()
        for i, line in enumerate(lines):
            if mode == 'hex':
                line_out = tohex(line)
                f2.write(line_out)
                f2.write("\n")
            elif mode == 'oct':
                line_out = tooct(line)
                f2.write(line_out)
                f2.write("\n")
                
print ("\n" + 'Amount of lines processed: ' + str(i))
print ('Script terminating')            


    
    
    
# Menu :
    # All of the file
    # Specific lines