'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Answer: 233168
'''

def sum_naturals():
    total_trey = 0
    total = 0

    for x in xrange(3, 1000, 3):
        value = str(x)
        if value[-1:] is '0':
            pass
        elif value[-1:] is '5':
            pass
        else:
            total_trey = total_trey + x
        
    print total_trey, 'total treys'
    print sum(range(5,1000,5)), 'sum 5 or 0'
    print total_trey + sum(range(5, 1000, 5))

# can also use value.endswith() for str

def sum_nat():
    sum_of_treys = 0
    for n in xrange(3, 1000, 3):
        # convert to string, check last digit
        n_string = str(n)
        if n_string[-1:] == '0':
            pass
        elif n_string[-1:] == '5':
            pass
        else:
            sum_of_treys = sum_of_treys + n
 
    return sum_of_treys + sum(range(5, 1000, 5))
        

if __name__ == '__main__':
    sum_naturals()
    print(sum_nat())
