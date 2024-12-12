import math

print("Name: ANTONY RAJU")
print("Admission no: 15")
print("Experiment no:6")


num=int(input("Enter a number"))
factorial=1
if(num<0):
    print("Factorial does not exit for negative number")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)

n1,n2=0,1
print("Fibnocci series",n1,n2,end="")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")
print()
total=0
list1=[]
n=int(input("Enter the list"))
for ele in range(0, n):
    ele=int(input())
    list1.append(ele)
for ele in range(0, len(list1)):
    total = total + list1[ele]
print("Sum of all elements in given list: ", total)

list2 = []
print("four digit numbers  with all their digits even and the number is a perfect square.")
for  i in range(1000,9999):
    sqrt_num=math.sqrt(i)
    if sqrt_num.is_integer():
        n = i
        flag = True
        while n != 0:
            r = n % 10
            if r % 2!=0:
                flag = False
            break
            n= n / 10

        if flag:
            list2.append(i)
print(list2)
