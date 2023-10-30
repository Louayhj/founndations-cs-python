num=int(input("enter a number : \n "))
# uncomment these lines for the first method i tried 
# newnum=str(num)
# length=len(newnum)
# print(length)
#
#second method 
count=0
temp=num
while num > 0 :
    num=num//10
    count=count+1
print(temp , " has " , count , " digits ")   
