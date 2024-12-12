print("antony raju \n roll no: 15")
color_list1_input=input("enter the first set of colors seperated by coma: ")
color_list1=color_list1_input.split(",")
color_list1=[color.strip() for color in color_list1]
if color_list1:
    print("first color: ",color_list1[0])
    print("last color: ",color_list1[-1])
else:
    print("no color entered")
color_list2_input=input("enter the second set of colors seperated by coma: ")
color_list2=color_list2_input.split(",")
color_list2=[color.strip() for color in color_list2]
unique_colors=[]
for color in color_list1:
    if color not in color_list2:
        unique_colors.append(color)

print("colors which are in color_list1 but not in color_list2 are: ",unique_colors)

color_integer=[]
count=1
for color in color_list1:
    color_integer.append(count)
    count+=1
print("integer list of color_list1 are: ",color_integer)

odd_integer=[]
for num in color_integer:
    if num%2!=0:
        odd_integer.append(num)
    count+=1
print("odd interger list from integer are: ",odd_integer)

