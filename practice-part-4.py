def max_num(x,y,z):
    if x > y:
        if x > z:
            return x
        else:
            return z
    else: 
        if y > z:
            return y
        else:
            return z
        
def mult_list(li):
    product = 1
    for num in li:
        product *= num
    return product

def rev_string(str):
    reverse = ""
    for char in str:
        reverse = char + reverse
    return reverse

def num_within(number, start, end):
    if number >= start and number <= end:
        return True
    else:
        return False
    
def pascal(n):
    li = [0,1,0]
    while n >= 1:
        print(li[1:-1])
        n -= 1
        li_copy = [0]
        for i in range(len(li)-1):
            a = li[i]
            b = li[i+1]
            c = a + b
            li_copy.append(c)
            # li_copy.append(li[i]+li[i+1])
        li_copy.append(0)
        li = li_copy

pascal(5)