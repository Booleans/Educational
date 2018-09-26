# Codewars - Beeramid
# https://www.codewars.com/kata/51e04f6b544cf3f6550000c1
# Let's pretend your company just hired your friend from college and paid you a referral bonus. Awesome!
# To celebrate, you're taking your team out to the terrible dive bar next door and using the referral bonus to buy, 
# and build, the largest three-dimensional beer can pyramid you can.
# And then probably drink those beers, because let's pretend it's Friday too.

# A beer can pyramid will square the number of cans in each level - 1 can in the top level, 4 in the second, 9 in the next, 16, 25...

def get_cans_for_row():
    '''
    Generator function to calculate the number of cans are required to build the next row of the pyramid.
    '''
    row = 1
    while True:
        yield row ** 2
        row += 1

def beeramid(bonus, price):
    '''
    INPUTS:
    bonus (int): Value of your bonus in dollars.
    price (float): Price per one can of beer.
    
    OUTPUT:
    row_num (int): The number of the last row in the pyramid that can be fully built with the given number of cans.
    '''
    if bonus <= 0:
        return 0
    n_cans = int(bonus // price)
    rows = get_cans_for_row()
    
    for row_num, row_width in enumerate(rows):
        if row_width > n_cans:
            return row_num
        else:
            n_cans -= row_width            
        