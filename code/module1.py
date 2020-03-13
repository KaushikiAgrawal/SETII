# =============================================================================
# built in installed packages
# =============================================================================
import sys
import logging
import numpy as np
import pandas as pd
sys.path.append("../scripts/")
from gensim.models import KeyedVectors
#logging.basicConfig(level=logging.DEBUG)
# =============================================================================
# import user made scripts and paths
# =============================================================================
import nGram
import myPreprossing as pre
import CosinDistanceSumForNGram as cosDistNGram
path = "C:\\Users\\prashantDhirendra\\set II\\data\\models\\"
file = "GoogleNews-vectors-negative300.bin"
modelAnsPath = "../data/workData/modelAns.csv"


# =============================================================================
# Load the pre-trained model from google or wikipidea
# =============================================================================
try :
    print("loading the pre trained model....")
    model = KeyedVectors.load_word2vec_format(path+file,binary=True)
    print("pre trained model loaded")
except FileNotFoundError as err:
    logging.critical("model not loaded")
    print(err)
    sys.exit()

# =============================================================================
# read the workData file and make nGrams
# =============================================================================
df = pd.read_csv("../data/workData/answerWiseSeprated/8.csv")
modelAnsDf = pd.read_csv(modelAnsPath,sep="\t")

minDistList = []
nGramValue = 1
while nGramValue <= 1:
    preProModelAns = pre.preProcessing(modelAnsDf.iloc[0].ModelAns.lower())
    nGramModelList = nGram.makeNGram(nGramValue,preProModelAns)
    modelAnsVector = cosDistNGram.findVector(model,nGramModelList)
    print(preProModelAns)
    print(nGramModelList)
    print(modelAnsVector[0])
#    print("Model - vector length",len(modelAnsVector))
    for i in range(df.shape[0]): 
        if i%100 == 0:
            print("minimun value calculated for ", i," answers",end="\n")
        preProAns = pre.preProcessing(df.iloc[i].EssayText.lower())
        nGramAnsList = nGram.makeNGram(nGramValue,preProAns)
        ansVector = cosDistNGram.findVector(model,nGramAnsList)
#        print(nGramAnsList)
#        print("Ans - ngram length",len(nGramAnsList))
#        print("Ans - vector length",len(ansVector))
        minDistList.append(cosDistNGram.calculate(modelAnsVector,ansVector))
    nGramValue +=1
df.insert(4,"minDistWithModelAns",minDistList,True)
df.to_csv("../data/workData/answerWiseSeprated/8.csv")