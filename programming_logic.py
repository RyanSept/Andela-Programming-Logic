#this generates prime numbers up to given parameter 'end'
#it returns a list
def prime_generator(end):
    if type(end)!=type(1):
        raise ValueError
    if end<=1:
        return []
    #empty list for storing generated numbers
    l = [2,]
    #we loop
    for n in range(0,end+1):
        if is_prime(n):
            l.append(n)
    return l

#this checks if a given value is prime, returns a boolean
def is_prime(num):
    #don't loop if even or less than 2
    if num%2==0 or num<2:
        return False
    if num==2 or num==3:
        return True
    else:
        #we loop from 2 to the number checking if it's divisible by 2
        #we return false if it is divisible, true if it's not
        for i in range(2,num):
            if num%i==0:
                return False
        return True


#this generates all prime numbers up to n
#for a non-fibonacci number, it returns a list with the last element as the
#fibonacci closest to it eg. if n=4 return = [0,1,1,2,3]
def fibonacci_generator(end):
    if type(end)!=type(1):
        raise ValueError
    if end<=1:
        return [end]
    next_fib = 0
    fibonacci_numbers = [0,1]
    #we loop through while our test case is not in the list of fibonacci numbers
    #and break when we reach or pass it
    while next_fib<end:
        next_fib = fibonacci_numbers[-1]+fibonacci_numbers[-2]
        if next_fib<=end:
            fibonacci_numbers.append(next_fib)
    return fibonacci_numbers

        
