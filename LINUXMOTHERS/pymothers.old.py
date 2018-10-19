#!/usr/bin/python


import sys
import os
import time
import shutil



# ######################################
# Constants and Var Init
cor_args_num = 1
base_file_in = "/home/tede/n55115/Joblib/Utils/file_processing/LINUXMOTHERS/motherstest.txt"
base_path_name1 = "/home/tede/n55115/Joblib/House_Keeping/Mothers/childs/"
full_origin_path = ""
copied_files = 0
nf_files = []
nf_dir = []






# #######################################
# Functions
def filetoliststrip(file):
    '''
  Function: filetoliststrip
  Description: Reads a file, stores in list (stripped)
  Input: File
  Output: List
  Usage: print (filetoliststrip("C:\\Users\\p.doulgeridis\\Desktop\\testpy.txt"))
  Notes: Path needs double \\ or reverse /
  '''
    file_in = str(file)
    lines = list(open(file_in, 'r'))
    content = [x.strip() for x in lines] 
    return (content, len(content)) 


def script_path_param(string1):
    '''
    Called as: script_path_param(sys.argv[0])
    '''
    import os
    script_name = os.path.basename(string1)
    script_dir = os.path.dirname(os.path.realpath(string1))
    script_full = string1
    return ( script_name, script_dir, script_full )
 
 
def script_time_param():
    import time
    # Name: time parameter
    # Function: script_time_param
    # Input: None
    # Output: string with formatted time
    # Usage: print (script_time_param) or a = script_time_param
    return time.strftime("%c")
 
def usage(string1):
    print ("\n" + "Name: " + str(os.path.basename(string1)))
    print ("Call as: " + str(os.path.basename(string1)) + " <FILE_IN> <FILE_OT> <SUB_START> <SUB_LENGTH> \n")
    return True	

def check_f_exists(inputpath, verbose = 'yes'):
    '''
    '''
    import os
    import sys
    check = 0
    
    if os.path.isfile(inputpath):
        check = 1
        
    if verbose == 'yes':
        if check == 1:
            print ("File located. Proceeding...")
            return True
        else:
            print ("File not located. Terminating...")
            sys.exit(5)
    else:
        if check == 1:
            return True
        else:
            return False

def check_d_exists(inputpath, verbose = 'yes'):
    import os
    import sys
    check = 0
    
    if os.path.isdir(inputpath):
        check = 1
    
    if verbose == 'yes':
        if check == 1:
            print ("Childs directory located. Proceeding...")
            return True
        else:
            print ("Childs directory not located. Terminating...")
            sys.exit(5)
    else:
        if check == 1:
            return True
        else:
            return False

# ############################################
# Main Job
print ("Script: " + script_path_param(sys.argv[0])[0] + " started at: " + script_time_param())
print ("Script directory: " + script_path_param(sys.argv[0])[1])
print ("Script Full Path: " + script_path_param(sys.argv[0])[2])

# Check if Mothers/childs directory exists
print ("\nChecking if child directory exists..")
check_d_exists(base_path_name1)

# Check if input file exists
print ("\nChecking if input exists..")
check_f_exists(base_file_in)

print ("\nAll initial checks succesful...initiating copies\n")
# Read input file in list
file_list = filetoliststrip(base_file_in)

# Calc expected n. of copies
expected_n_copies = file_list[1]


for child in file_list[0]:
    #print str(child)
    split_proc = child.split(";")
    #print split_proc[0]
    #print split_proc[1]
    origin_file = split_proc[0]
    destination_folder = split_proc[1]
    
    # print str(origin_folder)
    # print str(origin_file)
    # print str(destination_folder)
    
    #Check if destinaton folder exists, if not continue to next iteration and REPORT
    if not (check_d_exists(destination_folder, verbose = 'No')):
        print ("Copy directory: " + str(destination_folder) + " doesnt exist. Skipping...\n")
        nf_dir.append(destination_folder)
        continue
     
    
    # construct origin full filename
    full_origin_path = base_path_name1 + origin_file
    #print full_origin_path
    
    #Check if filename exists, if not continue to next iteration and REPORT
    if not (check_f_exists(full_origin_path, verbose = 'No')):
        print ("Copy file: " + str(origin_file) + " doesnt exist. Skipping...\n")
        nf_files.append(origin_file)
        continue
    
    try:
        print ("Copying: " + str(full_origin_path) + " to " + str(destination_folder) + "\n")
        shutil.copy(full_origin_path, destination_folder)
        copied_files += 1
    except:
        print ("Error copying file: " + origin_file)

        
        
# ###############################################
# Final Checks and Reporting

# print (copied_files)
# print (expected_n_copies)

if copied_files == expected_n_copies:
    print("Succesfully copied all files. Terminating")
else:
    print ("\nProblems during the process: \n")
    print ("Expected number of copies: " + str(expected_n_copies))
    print ("Actual number of succesful copies: " + str(copied_files))
    print ("\nNot found destination folders: \n")
    for j in nf_dir:
        print (j)
    print ("\nNot found origin child files: \n")
    for i in nf_files:
        print (i)