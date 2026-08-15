list=[1,-7,-4,3,67,32,567,0,98,678,-546,478]
largest=list[0]
index=0
for i in range(len(list)): # also we can use "for i, value in enumerate(list):"
    if(list[i]>largest):#comparing with largest number with list element one by one 
        largest=list[i] #if any number found large with respect to our initial largest number then update the largest variable
        index=i
print(largest, index)