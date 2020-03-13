# =============================================================================
# np.mean(model.wv["hello","world"],axis=0)
# =============================================================================

from scipy.spatial import distance
def calculate(modelAnsVector,ansVector):
    sum = 0
    for a in ansVector:
        minEachDist = distance.cosine(a,modelAnsVector[0])
        for ma in modelAnsVector:
            tempDist = distance.cosine(a,ma)
            minEachDist = min(minEachDist,tempDist)
            
        sum += minEachDist
    return sum
            
            
            
#print(modelAnsVector[0],ansVector[0],distance.cosine(modelAnsVector[0],ansVector[0]))
    
    
    
def findVector(model,arrList):
    vectorList=[]
    for i in range(len(arrList)):
        if arrList[i][0] in model.vocab:
            vectorList.append(model[arrList[i][0]])
#        else:
#            print(arrList[i][0])
    return vectorList