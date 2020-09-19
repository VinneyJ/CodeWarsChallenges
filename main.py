import collections

def comp(array1, array2):
    squared_num = [num ** 2 for num in array1]
    
    if collections.Counter(squared_num) == collections.Counter(array2):
      #print("Its working")
      return print("Its working")
    else:
        #print("its not working")
        return print("Not working")
    
    
a1 = [121, 144, 19, 161, 19, 144, 19, 11]

a2 = [121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19, 11*11]
    
comp(a1, a2)