from math import sqrt
def is_prime(number):
    prime = True
    for i in range(2,int(sqrt(number))+1):
        if number%i ==0 :
             prime = False
    return prime
print(is_prime(7))

def summention(number):
    summ = 0
    for i in range(2,number+1):
        if is_prime(i):
            summ = summ+i
    return summ
print(summention(12))



