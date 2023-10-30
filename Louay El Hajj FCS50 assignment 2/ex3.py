list1=[54,76,2,4,98,100]
int1=int(input("enter the first number : \n"))
int2=int(input("enter the seconde number : \n"))
for i in list1:
    if int1 <= i <= int2:
        print("\n" , i)