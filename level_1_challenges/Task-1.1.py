#Finding the sum of all the multiples of 3 or 5 below 1000
number = 1000
multiples_list = []

for i in range(1,number,1):
    if i % 3 == 0 or i % 5 == 0:
        multiples_list.append(i)
    else:
        continue

print(sum(multiples_list))



    
            
