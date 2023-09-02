marks= [ 12,76,90,25,97,23]
index = 0
for mark in marks:
    print(mark)
    if(index==4):
        print("wah bete wah")
    index+=1
# As we can see it is a long code and require much effort,so we use enumerate func() to save time and effort
for index ,mark in enumerate( marks):
    print(mark)
    if (index==5):
        print("Lanat olsun")
    index+=1

# EXAMPLE:2 we can manage index by using numerate func()
names=["hamza","talha","fayyaz","riaz","alia","pola"]
for index,name in enumerate(names,start=2):
    print(name)
    if index ==5 :
        print("sach ae bai sach ae")
    index+=1
