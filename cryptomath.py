# Cryptomath Module
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)
def gcd(a, b):
    # Return the GCD of a and b using Euclid's algorithm:
    # TODO
    return b

def findModInverse(a, m):
    # Return the modular inverse of a % m, which is
    # the number x such that a*x % m = 1.
    if gcd(a, m) != 1:
        return None # No mod inverse if a & m aren't relatively prime.
    # You can either use the slow method
    # step 1. Calculate a * b mod m for b values 0 through m-1
    # step 2. The modular inverse of a mod c is the b value that makes 
    #           a * b mod c = 1
    # Or using the extended Euclidean algorithm (advanced)
    b = 1
    # TODO
    return b 

