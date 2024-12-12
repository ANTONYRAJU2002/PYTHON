print("antony raju \n roll no: 15")
day=int(input("enter the day"))
month=int(input("enter the month"))
year=int(input("enter the year "))
print(day,";" ,month,";" ,year)
if(year%4==0) or (year%100!=0) and (year%400==0):
    print("the year is leap year")
else:
    print("the year is not leap year")