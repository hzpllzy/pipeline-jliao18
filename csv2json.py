import mycsv

header, data = mycsv.readcsv(mycsv.getdata())
#print(header)
#print(data)
print ("{\n", end = '')

print("  \"headers\":[", end = '')
wordcount=0
for words in header:
    if(wordcount!=0):
        print(",", end = '')
        print ("\"", end = '')
        print (words, end = '')
        print ("\"", end = '')
    else:
        print ("\"", end = '')
        print (words, end = '')
        print ("\"", end = '')
    wordcount=wordcount+1
print("],\n", end = '')
print("  \"data\":[\n", end = '')
rowcount=0
for rows in data:
    if(rowcount!=0):
        print("\n    },")
        print("    {\n", end = '')
        print("      ", end = '')
        headcount=0
        for words in rows:
            if(headcount!=0):
                print(", \""+header[headcount]+"\":\"", end = '')
                print(words+"\"", end = '')
            else:
                print("\""+header[headcount]+"\":\"", end = '')
                print(words+"\"", end = '')
            headcount=headcount+1
    else:
        print("    {\n", end = '')
        print("      ", end = '')
        headcount=0
        for words in rows:
            if(headcount!=0):
                print(", \""+header[headcount]+"\":\"", end = '')
                print(words+"\"", end = '')
            else:
                print("\""+header[headcount]+"\":\"", end = '')
                print(words+"\"", end = '')
            headcount=headcount+1
    rowcount=rowcount+1
print("\n    }\n", end = '')    
print("  ]\n", end = '')
print("}", end = '')


