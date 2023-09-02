# Pyhton provides several ways to manipulate files.some of them are:
# OPENING A FILE:
# python provides an open() function to open a file.It takes two arguments:the name of the file and the mode in
# which the file should be open. The mode can be 'r' for reading'w' for writing or 'a' for appending.
f = open('trash.py','r') #'r' is default mode which means that suppose if we do not put'r' in function,it is ok.
print(f)
text = f.read()
print(text)
f.close()
# in write mode,if we open a file which does not exist,python will make that file automatically
g= open('trash.py','w')
g.write('Hello,world!')
g.close()
# append mode 
h= open('trash.py','a')
h.write('hamza hu ')
h.close()

# THE "with" STATEMENT:
with open('trash.py','a') as h:
    h.write("i am inside")  # no need of "h.close()" type functions 
