import untangle
import mycsv

xml = untangle.parse(mycsv.getdata())

headers=xml.file.headers.cdata
headcount=len(xml.file.headers.cdata.split(','))

print(headers)

datacount=len(xml.file.data.record)



for row in range(datacount):
    for col in range(headcount):   
        data=xml.file.data.record[row].children[col].cdata
        if(col!=headcount-1):
            print(data+",",end='')
        else:
            print(data,end='')
    print("\n",end="")
