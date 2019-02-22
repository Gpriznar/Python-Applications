listA = [1,2,3,4,5]

listA += listA
print(listA)

#copy()
list1 = [1,2,3,4,5]
list2 = []

def duplicate():
    list2 = list1.copy()
    print(list1, list2)

duplicate()

#slicing

list3 = ["A", "B", "C", "D", "E"]
list4 = []

list4 = list3[:]

print(list3, list4)
