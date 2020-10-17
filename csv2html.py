import mycsv

header, data = mycsv.readcsv(mycsv.getdata())
#print(header)
#print(data)
print ("<html>\n<body>\n<table>\n<tr>")

for words in header:
    print("<th>")
    print (words)
    print("</th>")
    
print("</tr>\n")

for rows in data:
    print("<tr>")
    for words in rows:
        print("<td>")
        print(words)
        print("</td>")
    print("</tr>\n")
print("</table>\n</body>\n</html>")


