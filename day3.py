#Q1-target sum pair
#2 pair
pairs=[]
data=[15,2,20,30,7,80,25,10,35,3,11,5]
n=len(data)
target=int(input("Enter the target sum: "))
for i in range(n):
    for j in range(i+1,n):
        if data[i]+data[j]==target:
            pairs.append((data[i],data[j]))
if len(pairs)==0:
    print("None")
else:
    print(pairs)



#for n pairs
from itertools import combinations
data=[15,2,20,30,7,80,25,10,35,3,11,5]
pairs=[]
n=len(data)
target=int(input("Enter the target sum: "))
for i in range(2,n+1):
    for j in combinations(data,i):
        if sum(j)==target:
            pairs.append(j)
if len(pairs)==0:
    print("None")
else:
    print(pairs)



# You are given a list of time_intervals , representing booked meeting slots in a day , each interval is a list/tuple of 2 integers(start_time,end_time).Since some slots might overlap, your task is to consolidate the list and return the new list of non-overlapping intervals that cover all the origial booking times. Make a note that the intervals in the list are not guranteed to be sorted.
# constraints : input --> a list of intervals where each interval is a list of two integers range 1 - 24hrs
#  output --> the consolidated list with non-overlapping intervals

1,4 and 2,5
2,4 and 1,5

ip = [[2,3],[3,4],[1,4],[8,10],[2,5],[15,18],[7,8],[6,9]]
# ip = [[1,4],[2,5],[6,9],[8,10],[15,18]]
c = ip.copy()

op = [[1,5],[6,10],[15,18]]

def check(ip):
    for i in range(len(ip)):
        s_time,e_time = ip[i][0],ip[i][1]
        for j in range(len(ip)):
            if s_time < ip[j][0] < e_time < ip[j][1] :
                c.append([ip[i][0],ip[j][1]])
                c.remove(ip[i] )
                c.remove(ip[j])
            elif ip[j][0] < s_time < e_time < ip[j][1]:
                c.append([ip[j][0],ip[j][1]])
                c.remove(ip[i])
                c.remove(ip[j])
    print(sorted(c,key = lambda x:x[0]))

check(ip)


#merging the overlapping intervals:list of [start,end] return the new list of
#merged intervals sorted by time

#Q2->overlapping intervals
def merge_intervals(data):
    if not data:
        return []
    #step 1 -> sorting
    data_sorted=sorted(data,key=lambda x:x[0])
    merged=[data_sorted[0]]
    for current in data_sorted[1:]:
        last=merged[-1]
    
    #if current overlaps with last,merge them
        if current[0]<=last[1]:
            last[1]=max(last[1],current[1])
        else:
            merged.append(current[:]) #no overlap
    return merged

if __name__=="main_":
    input=[[1,3],[2,3],[8,10],[4,5],[15,18],[6,9]]
    merged_intervals=merge_intervals(input)
    print("Merged intervals are:",merged_intervals)
    

#lists,tuples,dictionaries,sets
#indexing,slicing,comprehensions

    

n=5
for i in range(n):   
    for j in range(n):
        if i==0 or i==n-1 or j==0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("  ", end="")
    for j in range(n):
        if j == 0 or   j==n-1 or (i==j  or i+j==n-1) and i<n-2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ",end="")
    for j in range(n):
        if i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for j in range(n):
        if i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#two lists are unique containing all elements present in a but not in b
def unique_elements(list1,list2):
    unique_list=[]
    for element in list1:
        if element not in list2:
            unique_list.append(element)
    return unique_list


a=[1,2,3,4,5,6]
b=[7,8,9,10,11,12]
for i in a:
    if i not in b:
        print(i,end="")
c=b-a
print(c)
sum=sum(c)
print("\n",sum)


#two lists are unique containing all elements present in a but not in b list a should contains all elements ,list b should be sum


