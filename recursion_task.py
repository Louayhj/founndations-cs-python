def binary(num):
    def binary_strings (num,st):
        if num==0:
            print(st)
        else:
            binary_strings(num-1,st  +"0")
            binary_strings(num-1,st  +"1")
    binary_strings(num,"")
num=int(input("enter a number : \n"))
print(binary(num))