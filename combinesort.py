print("Program to Merge two lists and sort it ")
num1=[23,66,72,21,12]
num2=[14,15,18,2,9]
print("the given lists are:",num1,num2)
num1.extend(num2)
print("The merged list is:",num1)
num1.sort()
print("The sorted list is",num1)
