import csv
print("Name : Antony raju\nRoll No : 15")
cs=open("f.csv","w")
cs.write("Antony,22,MCA\nAnnu,22,MCA")
cs.close()

f=open("f.csv","r")
csv_reader = csv.reader(f)

for row in csv_reader:
    print(row)