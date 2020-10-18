import sys

def getdata():
    if len(sys.argv)==1: # if no file given, read from stdin
        data = sys.stdin.read()
    else:
        f = open(sys.argv[1], "r")
        data = f.read()
        f.close()
    return data.strip()

def readcsv(data):
    """
    Read CSV with header from data string and return a header list
    containing a list of names and also return the list of lists
    containing the data.
    """
    headers=[]
    datatemp=[]
    row=""
    rowcount=0
    for characters in data:
        if(characters!='\n'):
            row=row+characters
        else:
            rowcount=rowcount+1
            if(rowcount==1):
                headers=row.split(",")
            else:
                datatemp.append(row.split(","))
            row=""
    #for row in data:
        #datatemp=datatemp+row
    datatemp.append(row.split(","))
    data=datatemp
    return headers, data