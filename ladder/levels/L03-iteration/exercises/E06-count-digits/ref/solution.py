def count_digits(number:int)->int:
    count=0
    while True:
        count+=1; number//=10
        if number==0: break
    return count

def digit_sum(number:int)->int:
    total=0
    while number>0: total+=number%10; number//=10
    return total
