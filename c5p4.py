import csv
print("Name : Antony raju\nRoll No : 15")
cs=open("f.csv","w")
cs.write("Antony,22,MCA\nAnnu,22,MCA")
cs.close()
c_to_read=[0,1]#this will read only the colomn with index 0 and 1
f1=open("f.csv","r")
csv_reader = csv.reader(f1)#to read the csv values
for row in csv_reader:
    sc=[row[i] for i in c_to_read]
    print(sc)