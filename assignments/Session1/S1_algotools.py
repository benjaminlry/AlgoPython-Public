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
        raise ValueError('No positive value found')
    average=valSum/nPositiveValues
    
    return average

    
#Test script for average_above_zero
test_tab_average=[1,2,3,-5]
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
        if val > 0:
            if val > numberMaxi:
                numberMaxi=val
    return numberMaxi

    
#Test script for average_above_zero
test_tab_max=[1,2,3,-5, 100]
maxPerso=max_value_perso(test_tab_max)
#print('Positive values average = '+str(moy))
print('Positive values max = {v}'.format(v=maxPerso))



"""
def average_above_zero(input_list):
    ##
    # compute the average of positive values
    # @input_list : the list of values to process
    # @return the average value of all the positive elements

    #init critical variable
    positive_values_sum=0
    positive_values_count=0

    first_item=input_list[0] #just a line to generate a code smell with an unused value

    #compute the average of positive elements of a list
    for item in input_list:
        #select only positive items
        if item>0:
            positive_values_sum+=item
            positive_values_count+=1
        elif item==0:
            print('This value is null:'+str(item))
        else:
            print('This value is negative:'+str(item))
    #compute the final average
    average=float(positive_values_sum)/float(positive_values_count)
    print('Positive elements average is '+str(average))
    return float(average)
"""

"""#testing average_above_zero function:
mylist=[1,2,3,4,-7]
result=average_above_zero(mylist)
message='The average of positive samples of {list_value} is {res}'.format(list_value=mylist,
                                                                          res=result)
print(message)
"""

def max_value(input_list):
    ##
    # basic function able to return the max value of a list
    # @param input_list : the input list to be scanned
    # @throws an exception (ValueError) on an empty list

    #first check if provided list is not empty
    if len(input_list)==0:
        raise ValueError('provided list is empty')
    #init max_value and its index
    max_val=input_list[0]
    max_idx=0
    #compute the average of positive elements of a list
    """for item in input_list:
        #select only positive items
        if max_val<item:
            max_val=item
    """
    #generic style : iterate over the range of list indexes
    for idx in range(len(input_list)):
        """if(input_list[idx] > 0):
        #select only positive items
            if max_val<input_list[idx]:
                max_val=input_list[idx]
                max_idx=idx"""

"""
    #generic style : iterate over the range of list indexes
    for idx, item in enumerate(input_list):
        #select only positive items
        if max_val<item:
            max_val=item
            max_idx=idx

    return max_val, max_idx
    """