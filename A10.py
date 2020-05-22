
list1 = [] 

for i in range (1, 101):
    if i % 2 == 0 :
        continue
    else : 
        list1.append(i)
        
print("list of add numbers ", list1)   
print("Sum ", sum(list1))