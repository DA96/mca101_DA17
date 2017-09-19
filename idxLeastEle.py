
def idxLeastEle(list,sIdx,fIdx):
    if(sIdx==fIdx):
        return sIdx
    elif(list[sIdx]<list[fIdx]):
        return idxLeastEle(list,sIdx,fIdx-1)
    else:
         return idxLeastEle(list,sIdx+1,fIdx)
        
