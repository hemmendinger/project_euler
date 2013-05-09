'''
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1£1 + 150p + 220p + 15p + 12p + 31p
How many different ways can £2 be made using any number of coins?
'''

# coin lists
# skip 2 pound note

list5 = [1,1,1,1,1]
denoms = [5,2,1]
count = 0


# while len(list5) <= 1:

item = list5.pop()
if item == 1:
    next = list5.pop()
    if next == 1:
        pass
    if next == 2:
        pass
    if next == 5:
        pass

'''
value = 5
count = 0
if (value - denom[0]) == 0:
    count += 1
elif:
    pass

value = 0

if value < 200:
    value = denom[0] + value
'''

def test(value):
    if value == 20:
        print 'yay'
        return
    elif value < 20:
        value = 2 + value
        print 'new value ', value
        test(value)
    else:
        print 'over 20'

def test2(value):
    denom = [10,5]
    incr = 0
    if value == 20:
        print 'yay'
        return
    elif value < 20:
        if (value + denom[incr]) < 20:
            value = value + denom[incr]
            print 'new ', value
            test2(value)
        else:
            print 'yo'
            if incr == len(denom):
                print 'not possible'
            incr += 1

 def backw(value, denom, goal):
     if value == 20:
         print 'yay'
         return
     elif value < 20:
         value = value + denom[1]
         print 'new value', value
         if value > 20:
             value = value + denom[0]
             print 'new value', value
             backw(value, denom, goal)
         backw(value, denom, goal)

def backwards():
    goal = 200
    denom_off = [1, 2, 5, 10, 20, 50, 100, 200]
    denom = [200, 100, 50, 20, 10, 5, 2, 1]
    value = 0
    count = 0
    current = 0
    if value == 200:
        count += 1
    if value < 200:
        value = value + denom[current]
        backwards()
    if value > 200:
        current += 1
        if current > len(denom):
            return count
        backwards()



'''
if __name__ == '__main__':
    denom = [25, 110]
    value = 0
    goal = 20
#    backw(value, denom, goal)
    for item in denom:
        
        backw(value, denom, goal)
'''
