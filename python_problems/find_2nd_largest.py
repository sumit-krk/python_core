list=[1,-7,-4,3,67,32,567,0,98,678,-546,478] #678, 567
first_largest=list[0]
second_largest=list[0]
for i, value in enumerate(list):
    if value > first_largest:
        second_largest=first_largest
        first_largest=value
    elif value > second_largest:
        second_largest=value
print(first_largest,second_largest)
