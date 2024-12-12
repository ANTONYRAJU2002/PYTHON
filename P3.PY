import math
print("antony raju \n roll no: 15")
a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
c=int(input("enter the third number: "))
n=max(a,b,c)
print("largest number is:",n)
nn=int(str(n)*2)
nnn=int(str(n)*3)
result= n+nn+nnn
print("n + nn +nnn=",result )
area=math.pi*n*n
perimeter=2*math.pi*n
volume=(4/3)*math.pi*n*n*n
print("area =",area )
print("perimeter =",perimeter)
print("volume =3",volume )