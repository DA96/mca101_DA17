
def idxLeastEle(list,sIdx,fIdx):
    '''
    Objective: To return the index of least element in list
    Input parameters: list
                      sIdx: starting index of list
                      fIdx: final index of list
    return value: index of least element in list
    '''
    #approach: using recursion
        
    if(sIdx==fIdx):
        return sIdx
    elif(list[sIdx]<list[fIdx]):
        return idxLeastEle(list,sIdx,fIdx-1)
    else:
        return idxLeastEle(list,sIdx+1,fIdx)
 
 
print('Index of least element in list is: ',idxLeastEle([6,2,8,1,3],0,4))
 
