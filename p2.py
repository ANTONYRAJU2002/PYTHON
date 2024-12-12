print("antony raju \n roll no: 15")
text=input("enter the line of text: ")
words = text.split()
word_count={}
for word in words:
    if word in word_count:
        word_count[word]+=1
    else:





























































        word_count[word]=1

words= text.split()
if len(words[0])>1:
    firstword=words[0][-1] + words[0][1:-1] + words[0][0]
else:
    firstword=words[0]
print("word count: ",word_count)
print("modified first word : ",firstword)
