#DSA-Exer-16

def find_decreasing_start(list1,start,end):
    #Remove pass and write your logic here
    for i in range(end):
        if list1[i+1]<list1[i]:
            return i+1

#Use different values for list1 and test your program
list1=[1,4,7,8,9,5,4]
start=0
end=len(list1)-1
result=find_decreasing_start(list1,start,end)
print("The index position at which the increasing array starts decreasing is:",result)
