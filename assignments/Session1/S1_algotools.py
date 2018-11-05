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



def roi_bbox(inputMat):    
    #input data type check
    if not(isinstance(inputMat, np.ndarray)):
        raise ValueError('Expected a numpy array as input')
    
    if not(inputMat.dtype==np.bool):
        raise ValueError('Expected input of type numpy boolean')
    
    lmin = inputMat.shape[0]
    lmax = 0
    cmin = inputMat.shape[1]
    cmax = 0
    
    for l in range(inputMat.shape[0]):
        for c in range(inputMat.shape[1]):
            #check line axis
            if inputMat[l,c] == True:
                if l<lmin:
                    lmin=l
                if l>lmax:
                    lmax=l
                if c<cmin:
                    cmin=c
                if c>cmax:
                    cmax=c
 
    roi = [[lmin,cmin],
           [lmin,cmax],
           [lmax,cmin],
           [lmax,cmax]]
                    
    return np.array(roi)
        
import numpy as np
inputMat=np.zeros((5,6),dtype=np.bool)
inputMat[2:4,3:5]=np.ones((2,2),dtype=np.bool)
print('inputMat='+str(inputMat))
roi=roi_bbox(inputMat)
print('roi='+str(roi))


def remove_whitespace(tab): 
    if not(isinstance(tab, list)):
        raise ValueError('Expected a list as input')
    
    for letter in tab:
        if letter == " ":
            tab.remove(letter)
    return tab

def test_remove_whitespace():
    testList=["a"," ","b","c","d"]
    import copy
    testListCopy = copy.deepcopy(testList)
    assert testList==remove_whitespace(testList)
    print('Remove whitespace = {i} => {o}'.format(i=testListCopy,o=testList))
test_remove_whitespace()

def test_remove_whitespace_empty():
    testList=[""]
    import copy
    testListCopy = copy.deepcopy(testList)
    assert testList==remove_whitespace(testList)
    print('Remove whitespace empty = {i} => {o}'.format(i=testListCopy,o=testList))
test_remove_whitespace_empty()




def roi_bbox(inputMat):    
    #input data type check
    if not(isinstance(inputMat, np.ndarray)):
        raise ValueError('Expected a numpy array as input')
    
    if not(inputMat.dtype==np.bool):
        raise ValueError('Expected input of type numpy boolean')
    
    lmin = inputMat.shape[0]
    lmax = 0
    cmin = inputMat.shape[1]
    cmax = 0
    
    for l in range(inputMat.shape[0]):
        for c in range(inputMat.shape[1]):
            #check line axis
            if inputMat[l,c] == True:
                if l<lmin:
                    lmin=l
                if l>lmax:
                    lmax=l
                if c<cmin:
                    cmin=c
                if c>cmax:
                    cmax=c
 
    roi = [[lmin,cmin],
           [lmin,cmax],
           [lmax,cmin],
           [lmax,cmax]]
                    
    return np.array(roi)
        
import numpy as np
inputMat=np.zeros((5,6),dtype=np.bool)
inputMat[2:4,3:5]=np.ones((2,2),dtype=np.bool)
print('inputMat='+str(inputMat))
roi=roi_bbox(inputMat)
print('roi='+str(roi))

def remove_whitespace_array(tab): 
    """
    this function remove whitespace in list

    @param : tab, list with whitespace
    @type : list
    
    @param : tab, list without whitespace
    @type : list
    """
    if not(isinstance(tab, list)):
        raise ValueError('Expected a list as input')
    
    for letter in tab:
        if letter == " ":
            tab.remove(letter)
    return tab

def test_remove_whitespace_array():
    testList=["a"," ","b","c","d"]
    import copy
    testListCopy = copy.deepcopy(testList)
    assert testList==remove_whitespace(testList)
    print('Remove whitespace array = {i} => {o}'.format(i=testListCopy,o=testList))
test_remove_whitespace()

def test_remove_whitespace_array_empty():
    testList=[]
    import copy
    testListCopy = copy.deepcopy(testList)
    assert testList==remove_whitespace(testList)
    print('Remove whitespace array empty = {i} => {o}'.format(i=testListCopy,o=testList))
test_remove_whitespace_empty() 

def remove_whitespace_string(string):
    """
    this function remove whitespace in string

    @param : string, string with whitespace
    @type : String
    
    @param : string, string without whitespace
    @type : String
    """
    if not(isinstance(string, str)):
        raise ValueError('Expected a list as input')
        
    return string.replace(' ', '')

def test_remove_whitespace_string():
    testString="a b cde f"
    testStringResult = remove_whitespace_string(testString)
    print('Remove whitespace string = {i} => {o}'.format(i=testString,o=testStringResult))
test_remove_whitespace_string()