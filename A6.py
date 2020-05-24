list1 = []
list2 = []
list3 = []

for n in range(1,21):
    list1.append(n)

print("Main list ",list1)

for i in list1: 
        if (i % 2 == 0): 
            list2.append(i) 
        else: 
            list3.append(i) 


print("Even list ", list2) 
print("Odd list ", list3) 
  