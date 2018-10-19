#!/usr/bin/python



import os
import sys

file_in = sys.argv[1]
start_r = sys.argv[2]
end_r = sys.argv[3]
file_ot = str(file_in) + ".trim"



def RemoveLines(fileName, start, end, file_ot):
    '''
    Name:
    Function:
    Description: 
    Input:
    Output:
    Usage:
    Notes:
    '''
    tempFile = open(fileName)
    tempList = []
    
    print(type(start))
    start = int(start)
    print(type(start))
    end = int(end)
    
    for lineNum, line in enumerate(tempFile):
        print(lineNum)
        if lineNum >= start and lineNum < end:
            continue  
        tempList.append(line)
    tempFile.close()
    tempFile = open(file_ot, 'w')
    tempFile.writelines(tempList)
    tempFile.close()
    
def RemoveLines_fast(file_in, start, end, file_ot):
    '''
    Name:
    Function:
    Description: 
    Input:
    Output:
    Usage:
    Notes:
    '''
    out_file = open(file_ot, 'w')
    
    print(type(start))
    start = int(start)
    print(type(start))
    end = int(end)
    
    
    with open(file_in, 'r') as fin:
        for lineNum, line in enumerate(fin):
            if lineNum >= start and lineNum < end:
                continue
            else:
                out_file.write(line)

    out_file.close()
    
#RemoveLines(file_in, start_r, end_r, file_ot)
RemoveLines_fast(file_in, start_r, end_r, file_ot)
