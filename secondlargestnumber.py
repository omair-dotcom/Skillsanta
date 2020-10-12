print("Program to find the second largest number in a list")
num=[22,74,23,44,12,9,12]
big1=num[0]
big2=num[0]
for i in range(1,len(num)):
    if num[i]>big1:
          big2=big1
          big1=num[i]
    elif num[i]>big2:
         big2=num[i]

print("The given list is:",num)
print("The second largest number is:",big2)
