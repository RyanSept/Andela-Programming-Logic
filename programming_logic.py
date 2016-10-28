#this generates prime numbers up to given parameter 'end'
#it returns a list
def prime_generator(end):
    #empty list for storing generated numbers
    l = []
    #we loop
    for n in range(0,end):
        if is_prime(n):
            l.append(n)
    return l

#this checks if a given value is prime, returns a boolean
def is_prime(num):
    if num%2==0:
        return False
    if num<2:
        return False
    if num==2 or num==3:
        return True
    else:
        #we loop from 2 to the number checking if it's divisible by 2
        #we return false if it is divisible, true if it's not
        for i in range(2,num):
            if num%2==0:
                return False
            return True


#this generates all prime numbers up to n
#for a non-fibonacci number, it returns a list with the last element as the
#fibonacci closest to it eg. if n=4 return = [0,1,1,2,3]
def fibonacci_generator(n):
    if n<=1:
        return [n]
    next_fib = 0
    fibonacci_numbers = [0,1]
    #we loop through while our test case is not in the list of fibonacci numbers
    while next_fib<n:
        next_fib = fibonacci_numbers[-1]+fibonacci_numbers[-2]
        if next_fib<=n:
            fibonacci_numbers.append(next_fib)
    return fibonacci_numbers

        
