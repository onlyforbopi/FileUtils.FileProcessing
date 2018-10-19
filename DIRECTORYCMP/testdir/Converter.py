#!/usr/bin/python

import sys


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
        print ('Correct number of arguments provided: ' + str(args_in_fixed))
        return True

        
def chck_args_type(string):
    '''
    Function : Checks the content of parameters
    Called as chck_args_type(string)
    '''
    return 0
        
def script_params(filename):
    '''
    Function: Prints all the basic script parameters
    Called as: script_params(sys.argv[0])
    Notes: Always returns true
    '''
    print ('Script name : ' + filename)
    print ('Processing')

    
# Initialize vars    
line_out = ''
counter1 = 0
counter2 = 0


# Parse arguments
print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

if not chck_args_num(len(sys.argv)):
    print ('Terminating Script....')
    sys.exit()

file_name = sys.argv[1]
outp_name = sys.argv[2]
mode = sys.argv[3]

# Basic script parameters
script_params(sys.argv[0])


# Open input file and output file
with open(file_name) as f1:
    with open(outp_name, 'a') as f2:
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