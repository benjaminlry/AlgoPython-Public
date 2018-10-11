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
        if val > 0:
            valSum+=float(val)
            nPositiveValues+=1
            
    if nPositiveValues <=0:
        """raise ValueError('No positive value found')"""
        average = 0;
    
    if nPositiveValues != 0:
        average=valSum/nPositiveValues
    
    return average

    
#Test script for average_above_zero
test_tab_average=[0,-7]
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

    
#Test script for average_above_zero
test_tab_max=[1,2,3,-5, 100]
maxPerso=max_value_perso(test_tab_max)
#print('Positive values average = '+str(moy))
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
    
    result_table=[]
    sizeTab = len(tab);
    actualPosition = sizeTab-1;
    while actualPosition >= 0:
        if len(tab) > 0:
                result_table.append(tab[actualPosition])
                actualPosition = actualPosition - 1 
    return result_table

    
#Test script for average_above_zero
test_tab_reverse=[1,2,3,-5, 100]
tab_reverse=reverse_table(test_tab_reverse)
#print('Positive values average = '+str(moy))
print('Tab reverse = {v}'.format(v=tab_reverse))
