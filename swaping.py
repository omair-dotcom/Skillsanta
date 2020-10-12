print("Program to swap the first and last value of a list")
num=[2,3,6,13,22,45,32]
print("The given list is:",num)
x=len(num)
a=num[0]
num[0]=num[6]
num[6]=a
print("The swaped numbers are :",a,num[0])
print("Result :",num)

