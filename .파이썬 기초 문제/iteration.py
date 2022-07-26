i=0
while True:
    i += 1
    if i>5:
        break;
    # for num in range(i):
    #     print("*", end=" ")
    # print('')
    print('*' * i)
    
A = [70,60,55,75,95,90,80,80,85,100]
total = 0
for score in A:
    total += score
average = total/len(A)
print(average)