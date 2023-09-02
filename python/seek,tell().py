#In python,the seek() and tell() functions are used to work with file objects and their positions within a file

# seek(): allows you to move the current position within a file to a specific point.the position is specified
# in bytes,and you can move either forward and backward from the current position.
# DEMO:
with open('mynewfile.txt','r') as f:
    #move to the 10th byte in the file
    f.seek(10)

    # read the next 5 bytes
    print(f.tell())     #gives us the value of seek
    data= f.read(5)
    print(data)
    print(type(f))


# tell function():Returns the current position within the file,in bytes.This can be useful for keeping tracks
# of your location within the file or for seeking to a specific postion related to the current postion.



# Truncate puts a limit on character to be allowed to write in a txt file while writing in a file.e.g.

with open('sample.txt','w') as f:
    f.write("Hello world!")
    f.truncate(5)



