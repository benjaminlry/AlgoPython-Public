##
#
# @author Alexandre Benoit, LISTIC Lab, IUT Annecy le vieux, FRANCE
# @brief a set of generic functions for data management

"""
# a variable
a=1 # default type : int
# an empty list
mylist = []
#a filled list
mylist2=[1,2,3]
#append to a list
mylist.append(10)
# a buggy list
mybuggylist=[1,'a', "Hi"]
#operators
b=a+2
mylist_sum=mylist+mylist2
"""

def average_above_zero(tab): 
    """
    Brief: computes the average with positiv value
    Args: 
        tab: a liste of numeric value exepcts at least one positive valus, raise expection
    Return: the computedd average
    Raises :
        ValueError if no positive value is found
        ValueError if input is not a list
    """
    if not(isinstance(tab, list)):
        raise ValueError('Expected a list as input')
        
    average=-99
    valSum=0.0 #initialize valSum to float
    nPositiveValues=0
    NMAX=len(tab) #get the size of tab
    
    for val in tab:
        """if isinstance(val, str):
            raise ValueError('No string value found')"""
        """if val >= 0:
            valSum+=float(val)
            nPositiveValues+=1"""
            
    if nPositiveValues <=0:
        """raise ValueError('No positive value found')"""
        average = 0
    
    if nPositiveValues != 0:
        average=valSum/nPositiveValues
        
    """if nStringValues == NMAX:
        average = 0"""
    
    return average
    
#Test script for average_above_zero
test_tab_average=["aa", "a"]
moy=average_above_zero(test_tab_average)
#print('Positive values average = '+str(moy))
print('Positive values average = {v}'.format(v=moy))


def max_value_perso(tab): 
    """
    Brief: computes the max with positiv value
    Args: 
        tab: a liste of numeric value exepcts at least one positive valus, raise expection
    Return: the max value
    Raises :
        ValueError if no positive value is found
    """
    if not(isinstance(tab, list)):
        raise ValueError('Expected a list as input')
    
    numberMaxi=0
        
    for val in tab:
        if val > numberMaxi:
            numberMaxi=val
    return numberMaxi

test_tab_max=[1,2,3,-5, 100]
maxPerso=max_value_perso(test_tab_max)

print('Positive values max = {v}'.format(v=maxPerso))



def reverse_table(tab): 
    """
    Brief: reverse input tab
    Args: 
        tab: a liste with values
    Return: the same liste with an other order
    """
    if not(isinstance(tab, list)):
        raise ValueError('Expected a list as input')
    
    
    sizeTab = len(tab);
    i = 0;
    while i+1 <= sizeTab/2:
        valueChange = tab[sizeTab-1-i]
        tab[sizeTab-1-i] = tab[i]
        tab[i] = valueChange
        i = i+1
    return tab

def test_revertTab_empty():
    testList=[]
    import copy
    testListCopy = copy.deepcopy(testList)
    assert testList==reverse_table(testList)
    print('ReverseTable empty = {i} => {o}'.format(i=testListCopy,o=testList))
test_revertTab_empty()

def test_revertTab_one():
    testList=[1]
    import copy
    testListCopy = copy.deepcopy(testList)
    assert testList==reverse_table(testList)
    print('ReverseTable one = {i} => {o}'.format(i=testListCopy,o=testList))
test_revertTab_one()

def test_revertTab_oddValue():
    testList=[1,2,3]
    import copy
    testListCopy = copy.deepcopy(testList)
    assert testList==reverse_table(testList)
    print('ReverseTable odd = {i} => {o}'.format(i=testListCopy,o=testList))
test_revertTab_oddValue()

def test_revertTab_evenValue():
    testList=[1,2,3,4]
    import copy
    testListCopy = copy.deepcopy(testList)
    assert testList==reverse_table(testList)
    print('ReverseTable even = {i} => {o}'.format(i=testListCopy,o=testList))
test_revertTab_evenValue()


