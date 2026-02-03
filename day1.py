def sum_of_list(nums):
    total=0
    for num in nums:
        total+=num
    print("sum is",total)
l=[1,2,3,4,5]
sum_of_list(l)

def attendance_summary(data):
    count_p=count_l=count_a=0
    for i in data:
        if i=='P':
            count_p+=1
        elif i=='L':
            count_l+=1
        elif i=='A':
            count_a+=1
    dict_data={
        'Present':count_p,
        'Late':count_l,
        'Absent':count_a
    }
    print("data",dict_data)
daily=["P","A","L","A","P","P","L","P","A","P"]
attendance_summary(daily)
# for dep store want to orgainze products before generating the report u will recieve list enter by staff 
# sometimes they enter them as strings () and
#  sometime as num waf clean_price that convert all values into integers 
# part 2 ignore invaid entries(something which is not convertedble into num) 
# part3 return list in sorted ascending order
def clean_price(data):
    clean_list = []
    for i in data:
        try:
            clean_list.append(int(float(i)))
        except:
            continue
    return sorted(clean_list)

list_data = [220,'120',360,'300.8','NO']
result = clean_price(list_data)
print("Cleaned and sorted prices:", result)

#a supermarket stores product prices in a list you must categorize each price into 
#1 price is less than 100 low
#2 greater than than equal to 100 and less than 500 -medium
#3 greater than equal to 500
#waf categorize that returns a new list of categories
def categorize(prices):
    categories = []
    for price in prices:
        if price < 100:
            categories.append("low")
        elif price >= 100 and price < 500:
            categories.append("medium")
        else:
            categories.append("high")
    return categories

prices_list = [50, 150, 600, 99, 500]
print("Categories:", categorize(prices_list))


#a teacher has a list of student marks you must return a filtered list of all marks that strictly above
#user given paassing score
#waf get_trishole that return only those values greater than trishole

def get_threshold(marks, threshold):
    filtered_marks = []
    for mark in marks:
        if mark > threshold:
            filtered_marks.append(mark)
    return filtered_marks

student_marks = [45, 78, 92, 55, 88, 35, 76]
passing_score = 76
print("Marks above threshold:", get_threshold(student_marks, passing_score))

for i in range(1,4):
    for j in range(1,4):
        print("*",end="")
    print()
        
for i in range(1,4):
    for j in range(1,i+1):
        print("*",end="")
    print()

for i in range(1,4):
    for j in range(1,4):
        if i==j:
            print("*",end="")
        else:
            print(" ",end=" ")
    print()

for i in range(1,4):
    for j in range(1,4):
        if j==(4-i):
            print("*",end="")
        else:
            print(" ",end=" ")
    print()

for i in range(0,3):
    for j in range(0,3):
        if i==j or i+j==2:
            print("*",end="")
        else:
            print(" ",end=" ")
    print()

#hallow square
for i in range(1,6):
    for j in range(1,6):
        if i==1 or i==5 or j==1 or j==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#pattern printing
#  @
# @ @
#@   @
#*   *
#*   *
#*   *
#@   @
# @ @c
#  @

n=3
for i in range(n):
    for j in range(n):
        if(i+j==n-1):
            print("@",end=" ")
        else:
            print(" ",end=" ")
    for j in range(n,2*n-1):
        if(j-i==n-1):
            print("@",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(n):
    for j in range(2*n-1):
        if(j==0 or j==2*n-2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
        
for i in range(n):
    for j in range(n):
        if(i==j):
            print("#",end=" ")
        else:
            print(" ",end=" ")
    for j in range(n,2*n-1):
        if(i+j==2*n-2):
            print("#",end=" ")
        else:
            print(" ",end=" ")
    print()  





# @ @
#@   @
#*   *
#*   *
#*   *
#@   @
# @ @c
#  @

n=3
for i in range(n):
    for j in range(n):
        if(i+j==n-1):
            print("@",end=" ")
        else:
            print(" ",end=" ")
    for j in range(n,2*n-1):
        if(j-i==n-1):
            print("@",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(n):
    for j in range(2*n-1):
        if(j==0 or j==2*n-2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
        
for i in range(n):
    for j in range(n):
        if(i==j):
            print("#",end=" ")
        else:
            print(" ",end=" ")
    for j in range(n,2*n-1):
        if(i+j==2*n-2):
            print("#",end=" ")
        else:
            print(" ",end=" ")
    print()  


n=int(input())
if n&1==0:
    print("even")
else:
    print("odd")
def get_threshold(marks, threshold):
    filtered_marks = []
    for mark in marks:
        if mark > threshold:
            filtered_marks.append(mark)
    return filtered_marks

student_marks = [45, 78, 92, 55, 88, 35, 76]
passing_score = 76
print("Marks above threshold:", get_threshold(student_marks, passing_score))

