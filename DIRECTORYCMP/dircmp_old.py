##########################################################################
#   DIRECTORY COMPARE V.1                                                #
#                                                                        #
#   Usage :                                                              #
#                                                                        #
#   python DirComp.py <dir1> <dir2>                                      #
#                                                                        #
#   Function :                                                           #
#                                                                        #
#   Sizes and compares directories based on filenames, prints out the    #
#   filenames that only exist in one directory of the two, for both      #
#   directories.                                                         #
#                                                                        #
#   Notes :                                                              #
#                                                                        #
#   Main function is "build_files_set" which takes a directory as input  #
#   and parses each file name in full path, relative path, and assigns   #
#   them to a set so we can do set operations.                           #
#                                                                        #
#   The compare_directories function simply calculates the differences   #
#   between the given sets.                                              #
#                                                                        #
#   Modules:                                                             #
#                                                                        #
#   import os                                                            #
#   import sys                                                           #
#   import re                                                            #
#   import subprocess                                                    #
#   import time                                                          #
##########################################################################




import os
import sys
import re
import subprocess
import time
import collections

# Get the script path
def get_script_path():
    return os.path.dirname(os.path.realpath(sys.argv[0]))

# Parse files of directory
def build_files_set(rootdir):
    root_to_subtract = re.compile(r'^.*?' + rootdir + r'[\\/]{0,1}')
    # Assign relative paths to set for comparison
    files_set = set()
    for (dirpath, dirnames, filenames) in os.walk(rootdir):
        for filename in filenames + dirnames:
            full_path = os.path.join(dirpath, filename)
            relative_path = root_to_subtract.sub('', full_path, count=1)
            files_set.add(relative_path)

    return files_set

# Compare sets 
def compare_directories(dir1, dir2):
    files_set1 = build_files_set(dir1)
    files_set2 = build_files_set(dir2)
    return (files_set1 - files_set2, files_set2 - files_set1)

    
def compare_bool(dir1, dir2):
    files_set1 = build_files_set(dir1)
    files_set2 = build_files_set(dir2)
    compare = lambda dir1, dir2: collections.Counter(files_set1) == collections.Counter(files_set2)
    return compare
    
def are_eq(a, b):
    files_set1 = build_files_set(a)
    files_set2 = build_files_set(b)
    return set(a) == set(b) and len(a) == len(b)    
    
    
# Get size - Not working
def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size
 
# call to system du - working
def du(path):
    """disk usage in human readable format (e.g. '2,1GB')"""
    return subprocess.check_output(['du','-sh', path]).split()[0].decode('utf-8') 
    

def main():
    
    if __name__ == '__main__':

    # ##
    # Script parameters 
        print (' ')
        print ("Script run at: " + str(time.strftime("%H:%M:%S")))
        print ("Script run from: " + get_script_path())
    
    # ##
    # Process arguments
        print (' ')
        total = len(sys.argv)
        cmdargs = str(sys.argv)
    # print ("The total numbers of args passed to the script: %d " % total)
    # print ("Args list: %s " % cmdargs)
    
    # print ("Script name: %s" % str(sys.argv[0]))
    # print ("First argument: %s" % str(sys.argv[1]))
    # print ("Second argument: %s" % str(sys.argv[2]))

        dir1 = str(sys.argv[1])
        dir2 = str(sys.argv[2])
    
    # DEBUG
    # dir1 = '/home/tede/n55115/PD/UTILS/DirectoryComparison/ORIGINFOLDERa'
    # dir2 = '/home/tede/n55115/PD/UTILS/DirectoryComparison/BATCHINFO'
    
    # ##
    # Compare Directories
        in_dir1, in_dir2 = compare_directories(dir1, dir2)

    # ## 
    # Output 
        print (' ')
        print 'Comparing Files: '
        print (dir1)
        print (dir2)
    
    
        print (' ')
        print 'Comparing sizes: ' 
        size1 = du(dir1)
        size2 = du(dir2)
        print ("Directory " + dir1 + " size: " + str(size1))
        print ("Directory " + dir2 + " size: " + str(size2))
    
        print '\nFiles only in {}:'.format(dir1)
        for relative_path in in_dir1:
            print '* {0}'.format(relative_path) 

        print '\nFiles only in {}:'.format(dir2)
        for relative_path in in_dir2:
            print '* {0}'.format(relative_path)
    
    # Boolean
        return are_eq(dir1, dir2)
    
main()

print main()