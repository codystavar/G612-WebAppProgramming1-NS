#function
def second_largest(list):
    large= max(list)
    list.remove(large)
    large= max(list)
    return large


#input of list
li=[]
n=int(input("Enter size of list "))
for i in range(n):
    e=int(input("Enter element of list "))
    li.append(e)

#smallest
print("second largest in ",li,"is")
print(second_largest(li))