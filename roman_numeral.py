
def conv(n, level):
    """ Given decimal level :
        1 - 0
        10 - 1
        100 - 2
        1000 - 3
        etc...
        and a digit 0-9, returns roman numeral equivalent

        so say passing in 400 is conv(4,3)
    """
        
    V = 'IVXLCDM'
    if (level == 3 and n > 3) or level > 3:
        return 'M'*n*10**(level-3)
    elif n < 4:
        return V[level*2]*n
    elif n == 4:
        return V[level*2]*(5-n)+V[level*2+1]
    elif n < 8:
        return V[level*2+1]+V[level*2]*(n-5)
    else:
        return V[level*2]*(10-n)+V[level*2+2]


def roman(num):
    """ Convert integer number to string containing Roman Numeral value
        ex. 1903 -> 'MCMIII'
        For numbers > 1000, string size increases linearly with every 1000s (add an M)s
    """
    if num<0 or type(num)!=int:
        return None
    return ''.join([conv(int(digit),i) for i,digit in enumerate(str(num)[::-1])][::-1])


def unroman(rom):
    """ Convert string Roman Numberals back to integer number
        ex. 'MCMIII' -> 1903
    """
    if rom == None:
        return None
    R = dict( zip( 'IVXLCDM', [1,5,10,50,100,500,1000] ) )
    lastmax = 0
    total = 0
    for x in str(rom)[::-1]:
        if R[x] < lastmax:
            total -= R[x]
        else:
            total += R[x]
            lastmax = R[x]
    return total
        

#tests = [1,2,3,4,5,6,7,8,9,10, 1910,1954,1990, 2012, 2013, 391349,1000000]
tests = [x for x in range(-1,20)] + [x**2 for x in range(5,60)]
for test in tests:
    print test,":",roman(test),':',unroman(roman(test))
