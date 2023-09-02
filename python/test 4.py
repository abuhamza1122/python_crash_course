# Write a python program to translate a messageinto secret code language.Use the code below to translate normal
# english into secret code language

# Coding:
# if the word contains only 3 characters,remove the 1st letter and append it at the end.
# now append three random characters at the starting and end.
# else:
# simply reverse the strings 

#Decoding:
# if the word contains less than three characters,reverse it. 
# else:
# remove three random characters from start and end



#CODING LANGUAGE:
coding = False # all depend whether the coding is true on false
st= input("enter your message:")
words= st.split(" ") 
if coding:
  nwords=[]
  for word in words:
     if(len(word)>=3):
        r1="dus"      #random word 1
        r2="wjn"      #random word 2
        stnew = r1 +word[1:] +word[0] +r2
        nwords.append(stnew)
  else:
        nwords.append(word[::-1])
        print("".join(nwords))
#decoding

else:
  nwords=[ ]
  for word in words:
     if(len(word)>=3):
        stnew =  word[3:-3] 
        stnew =stnew[-1] +stnew[:-1]
        nwords.append(stnew)
  else:
        nwords.append(word[::-1])
        print("".join(nwords))
