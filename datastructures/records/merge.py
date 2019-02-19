from createFile import *

def mergeSort(blockSize,f1,f2,f3):
    '''
    Objective : To merge two sorted records one from f1 and one from f2 each of size 'blockSize'
                and write it to f3 in sorted manner
    Input:
         f1: File pointer for reading records from first file
         f2: File pointer for reading records from second file
         f3: File pointer for writing records to third file
    '''

    #MergeSort
    #print(blockSize,len(lst1),len(lst2))
    rec1 = None
    rec2 = None 
    last_loc1 = f1.tell()
    last_loc2 = f2.tell()
    i,j=0,0
    
    while i<blockSize and j<blockSize:
        last_loc1 = f1.tell()
        last_loc2 = f2.tell()
        try:
            rec1 = pickle.load(f1)
        except EOFError:
            i = blockSize
            break
        try:
            rec2 = pickle.load(f2)
        except EOFError:
            f1.seek(last_loc1)
            j = blockSize
            break
        
        if rec1.getKey() < rec2.getKey():
            pickle.dump(rec1,f3)
            f2.seek(last_loc2)
            i+=1
        else:
            pickle.dump(rec2,f3)
            f1.seek(last_loc1)
            j+=1

    while i<blockSize:
        try:
            pickle.dump(pickle.load(f1),f3)
            i+=1
        except EOFError:
            break

    while j<blockSize:
        try:
            pickle.dump(pickle.load(f2),f3)
            j+=1
        except EOFError:
            break
    


def mergeFile(file1,file2,file3,file4,blockSize,nRecords):
    '''
    Objective: To merge files
    Input:
        nRecord : number of records
        blockSize: initial blockSize
    Return : None
    '''
    f1 = open(file1,'rb')
    f2 = open(file2,'rb')
    f3 = open(file3,'ab')
    f4 = open(file4,'ab')
    temp = 0
    blockSize=4

    #Merging records using mergesort until blocksize <= nRecord
    while nRecords//blockSize:
        count = 0
        while count < nRecords:
            mergeSort(blockSize,f1,f2,f3)
            mergeSort(blockSize,f1,f2,f4)
            count+=blockSize*4
        f1Name = f1.name
        f2Name = f2.name

        f1.close()
        f2.close()
        os.remove(f1Name)
        os.remove(f2Name)
        f3.close()
        f4.close()

        blockSize*=2        
        if temp == 0:
            f1 = open(file3,'rb')
            f2 = open(file4,'rb')
            f3 = open(file1,'ab')
            f4 = open(file2,'ab')
            temp = 1
        else:
            f1 = open(file1,'rb')
            f2 = open(file2,'rb')
            f3 = open(file3,'ab')
            f4 = open(file4,'ab')
            temp = 0

    if temp == 0:
        f1 = open(file1,'rb')
    else:
        f1 = open(file3,'rb')

    lower= int(input('Enter the lower limit of record:'))
    upper= int(input('Enter the upper limit of record:'))
    if upper>nRecords:
        print("Out of range")
        return

    pickle.load(f1)
    size = f1.tell()
    f1.seek(size*(lower))
    for i in range(lower,upper):
        print(pickle.load(f1))

if __name__=="__main__":
    blocksize=4
    file1="File1.txt"
    file2="File2.txt"
    file3="File3.txt"
    file4="File4.txt"
    mergeFile(file1,file2,file3,file4,blocksize,nRecords)
