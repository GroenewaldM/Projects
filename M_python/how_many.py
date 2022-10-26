animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    i = 0
    prev_i = 0
    values = aDict.values()
    key = aDict.keys()
    copy_aDict = aDict

    
    for thing in aDict:
        ans = thing
        i = 0
        for things in aDict[thing]:
            i = i + 1
        if i > prev_i:
            prev_i = i
            ans = thing
        
    return ans

print(how_many(animals))