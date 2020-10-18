import mycsv

header, data = mycsv.readcsv(mycsv.getdata())
#print(header)
#print(data)
print ("<?xml version=\"1.0\"?>\n<file>\n", end = '')

print("  <headers>", end = '')
wordcount=0
for words in header:
    if(wordcount!=0):
        print(",", end = '')
        print (words, end = '')
    else:
        print (words, end = '')
    wordcount=wordcount+1
print("</headers>\n", end = '')
print("  <data>\n", end = '')
for rows in data:
    print("    <record>\n", end = '')
    print("      ", end = '')
    headcount=0
    for words in rows:
        print("<"+header[headcount]+">", end = '')
        print(words, end = '')
        print("</"+header[headcount]+">", end = '')
        headcount=headcount+1
    print("\n    </record>\n", end = '')
print("  </data>\n", end = '')
print("</file>", end = '')


