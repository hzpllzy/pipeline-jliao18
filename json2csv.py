import json
import mycsv

js = json.loads(mycsv.getdata())

headers=js['headers']
headcount=0
for head in headers:
    if(headcount==0):
        print(head,end='')
    else:
        print(","+head,end='')
    headcount=headcount+1
print()

data=js['data']

for row in data:
    colcount=0
    for col in row.values():
        if(colcount==0):
            print(col,end='')
        else:
            print(","+col,end='')
        colcount=colcount+1
    print()

