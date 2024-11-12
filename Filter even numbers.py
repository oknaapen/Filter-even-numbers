#make a list
list = [3,2,56,300,94,67,23,44,56,35,45]

#collect the even numbers list
even = []

#loop the list
for i in list:
    #filter the even numbers
    if i % 2 == 0:
        even.append(i)

#display list even
print(even)