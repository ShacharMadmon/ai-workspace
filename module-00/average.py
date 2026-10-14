def average(numbers):
    cnt = 0
    num_sum = 0
     
    
    if len(numbers) == 0:
        return None
     
    for n in numbers:
        cnt = cnt + 1
        num_sum = num_sum + n
            
    avg = num_sum / cnt
    return avg
print(average([100,200,500]))
print(average([17,23,54]))
print(average([]))
print(average([7]))
