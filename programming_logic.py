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
    if num<2:
        return False
    if num==2:
        return True
    if num%3 == 0:
        return False
    else:
        #we loop from 2 to the number checking if it's divisible by 2
        #we return false if it is divisible, true if it's not
        for i in range(2,num):
            if num%2==0:
                return False
            return True

print prime_generator(10001)
