import random
numbers=[]
for i in range(30):
    num=random.randint(-30,30)
    numbers.append(num)
print(numbers)
c  = 0
for i in range(30):
    for j in range(i+1,30):
        for k in range(j+1,30):
            if numbers[i]+numbers[j]+numbers[k]==0:
                print('Η τριάδα '+str(numbers[i])+' '+str(numbers[j])+' '+str(numbers[k])+' έχει άθροισμα  0')
                c+=1


if c==0 :
    print('Δεν υπάρχει τριάδα με άθροισμα 0')
                      
                          
            
            

    
