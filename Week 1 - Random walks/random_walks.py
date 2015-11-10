import random
def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    # Your code here
    x = random.choice(range(0,102,2))
    
    return x


print(genEven())

def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    x = 10
    
    return x
