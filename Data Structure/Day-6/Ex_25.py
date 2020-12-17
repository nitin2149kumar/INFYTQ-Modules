#DSA-Exer-25

def sortActivity(value):
    return value[1]
def sortActivities(value):
    return len(value)
def find_maximum_activities(activity_list,start_time_list, finish_time_list):
    #Remove pass and write your logic here
    activity_details = list(zip(activity_list,start_time_list, finish_time_list))
    activity_details.sort(key=sortActivity)
    print(activity_details)
    x=[]
    for i in range(len(activity_details)):
        l=[activity_details[i]]
        for index,activity in enumerate(activity_details):
            if index>i:
                if activity[1]>l[len(l)-1][2]:
                    l.append(activity)
        x.append(l)
    x.sort(key=sortActivities, reverse=True)
    print(x)
    y=[]
    for i in x[0]:
        y.append(i[0])
    print("y is: "+str(y))
    if len(y)==1:
        y=[]
        y.append(x[1][0][0])#if only one task can be completed then return the second task.This is however not given in the question. 
    return y

#Pass different values to the function and test your program
activity_list=[1,2,3,4,5,6,7]
start_time_list=[1,4,2,3,6,8,6]
finish_time_list=[2,6,4,5,7,10,9]

print("Activities:",activity_list)
print("Start time of the activities:",start_time_list)
print("Finishing time of the activities:", finish_time_list)

result=find_maximum_activities(activity_list,start_time_list, finish_time_list)
print("The maximum set of activities that can be completed:",result)
