####take the input

num =input()
array =input().split()  

#takethe set to get unique values 
s1=set()  
s2=set()  

###
for i in array:
    if  i in s1:
        s2.add(i)
    else:
        s1.add(i)
s3=s1.difference(s2)
print(s3.pop())