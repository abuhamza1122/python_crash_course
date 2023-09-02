# readline() is used to read the files 
H= open('myfile.txt','r')
while True:
    line= H.readline()
    print(line)
    if not line:
        break 

# demo2:
f= open('mynewfile.txt','r')
i = 0
while True:
    i = i + 1
    line= f.readline()
    if not line:
        break
    m1=line.split(",")[0]
    m2=line.split(",")[1]
    m3=line.split(",")[2]
    print(f"Marks of student {i} in maths is:{m1}")
    print(f"Marks of student {i} in english is:{m2}")
    print(f"Marks of student {i} in SST is:{m3}")
    print(line)
# writelines():
# for minimum lines
f = open('file2.txt','w')
lines= ['line1\n','line2\n','line3\n']
f.writelines(lines)
f.close()

