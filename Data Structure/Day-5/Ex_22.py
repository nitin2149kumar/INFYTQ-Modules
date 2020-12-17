#DSA-Exer-22

def order_heights(student_list,height_list):
    #Write your logic here
    for i in range(len(height_list)-1):
        for j in range(len(height_list)-1):
            min_index=height_list.index(min(height_list[i:]))
        height_list[i],height_list[min_index]=height_list[min_index],height_list[i]
        student_list[i],student_list[min_index]=student_list[min_index],student_list[i]
    return[student_list,height_list]

#Pass different values to the function and test your program
student_list=["Santa","Tris","Arun","Rachel","John"]
height_list=[132.7,129.2,135,130.6,140]
print("Initial student details :")
print("The students:",student_list)
print("Their heights:",height_list)
print()
result=order_heights(student_list,height_list)
print("After arranging the students in the order of their height:")
print("The students :",result[0])
print("Their heights:",result[1])
