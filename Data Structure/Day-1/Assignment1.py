#DSA-Assgn-1

def merge_list(list1, list2):
    merged_data=""
    #write your logic here
    for x,y in zip(list1,list2[::-1]):
        if x==None:
            merged_data+=" "+y
        elif y==None:
            merged_data+=" "+x
        else:
            merged_data+=" "+x+y
        resultant_data=merged_data[1:]
    return resultant_data

#Provide different values for the variables and test your program
list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
list2=['y','tor','e','eps','ay',None,'le','n']
merged_data=merge_list(list1,list2)
print(merged_data)
