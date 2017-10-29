

def merge2SortedLists(list1,list2,list3,ind1=0,ind2=0):

    '''
    Objective: To merge two sorted lists into one sorted list
    Input parameters:
                     list1 : sorted list 1                     
                     list2 : sorted list 2                     
                     list3 : empty list 3
                     
                     ind1 : index of list 1
                     ind2 : index of list 2
                    
    Return value: list3 which is merged from 2 lists and is a sorted list
    '''
    #approach: recursion
    
    len1=len(list1)
    len2=len(list2)
    
    if(ind1==len1):
        list3.extend(list2[ind2:])
        return list3
    
    if(ind2==len2):
        list3.extend(list1[ind1:])
        return list3
                            
    if(list1[ind1]<list2[ind2]):
        list3.append(list1[ind1])
        return merge2SortedLists(list1,list2,list3,ind1+1,ind2)
    else:
        list3.append(list2[ind2])
        return merge2SortedLists(list1,list2,list3,ind1,ind2+1)
        
    


def main():
    '''
    Objective: To merge 2 sorted lists into one sorted list
    Input parameters: none
    Return value: none
    '''
    l1=[10,20,30,40,50]
    l2=[5,9,12,22,26,34,78,90]
    l3=[]

    print(merge2SortedLists(l1,l2,l3))

if __name__=='__main__':
    main()

    
