'''


Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size, find the numerator of the fraction immediately to the left of 3/7.



    '''
'''
 # Brute force, works with low numbers   
def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

        Unless b==0, the result will have the same sign as b (so that when
        b is divided by it, the result comes out positive).
        """
    while b:
        a, b = b, a % b
    return a

def simplify_fraction(numer, denom):

    # Remove greatest common divisor:
    common_divisor = gcd(numer, denom)
    (reduced_num, reduced_den) = (numer / common_divisor, denom / common_divisor)
    # Note that reduced_den > 0 as documented in the gcd function.

    return reduced_num/ reduced_den

def GeneratingFractions(x,y,n):
    #x is a numerator (3) and y is the denominator (7) upto which we want to generate fractions upto n (1000000)
    new_list = []
    desired_max = x/y
    for i in range(1, n):
        for j in range(n-1,i, -1):
            new_fraction = i / j
            if new_fraction < desired_max:
                new_list.append(new_fraction)
            else:
                break
    new_list.sort()
    return new_list[-1]
'''
'''
#A variation of Stern_Brocot_tree, again good for small numbers 
def Stern_Brocot(x,y,n):
    states = [(0, 1, 1, 1)]
    result = []
    while len(states) != 0:
        a, b, c, d = states.pop()
        if a + b + c + d <= n or (a+c <= x and b + d <= y):
            result.append((a+c, b+d))
            states.append((a, b, a+c, b+d))
            states.append((a+c, b+d, c, d))
    my_index = result.index((x,y))
    my_result = result[my_index-1][0]
    return my_result
'''

def GeneratingFractions(x,y,n):
    #need to find p, p/q<x/y or p = (xq  -1)/y
    r = 0
    s = 1
    
    result = 0
    for q in range(n,2, -1):
        p = (x*q - 1)/y
        if p*s > r*q and int(p) == p:
            s,r = q, p
            result = p
    return result

final = GeneratingFractions(3, 7, 1000000 )
print(final)
