import time
timestamp=time.strftime('%H:%M:%S')
print (timestamp)
hour= int(time.strftime('%H'))
print(timestamp)
minute=int(time.strftime('%M'))
print(timestamp)
second=int( time.strftime('%S'))
print(timestamp)
if (hour>=2 and hour<5):
    print("good evening  sir")
else:
    print("good night sir")
