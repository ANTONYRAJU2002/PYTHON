print("Name: antony raju")
print("Roll No: 015")

dict1 = {}
n=int(input("enter the number of items for dict 1: "))

for _ in range(n):
    key= input("enter the key: ")
    value= (input("enter the value: "))
    dict1[key]=value

asc_order = dict(sorted(dict1.items()))
print("Ascending order by keys:", asc_order)

des_order = dict(sorted(dict1.items(), reverse=True))
print("Descending order by keys:", des_order)

dict2 = {}
m=int(input("enter the number of items for dict 2 : "))

for _ in range(m):
    key= input("enter the key: ")
    value= (input("enter the value: "))
    dict2[key]=value


merged_dict = {**dict1, **dict2}
print("Merged dictionary:", merged_dict)