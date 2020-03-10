# =============================================================================
# built in installed packages
# =============================================================================
import sys
import logging
import pandas as pd
sys.path.append("../scripts/")
from gensim.models import KeyedVectors
logging.basicConfig(level=logging.DEBUG)
# =============================================================================
# import user made scripts and paths
# =============================================================================
import nGram
path = "C:\\Users\\prashantDhirendra\\set II\\data\\models\\"
file = "GoogleNews-vectors-negative300.bin"

# =============================================================================
# read the workData file
# =============================================================================
df = pd.read_csv("../data/workData/answerWiseSeprated/5.csv")
#for i in range(df.shape[0]):
#    temp = df.iloc[863].EssayText
#    print(nGram.makeNGram(2,temp))
 
Ans2Gram = nGram.makeNGram(2,df.iloc[1].EssayText)
print(Ans2Gram[1][0])


# =============================================================================
# Load the pre-trained model from google or wikipidea
# =============================================================================
try :
    print("loading the pre trained model....")
    model = KeyedVectors.load_word2vec_format(path+file,binary=True)
    print(model.wv[Ans2Gram[1]])
except FileNotFoundError as err:
    logging.critical("model not loaded")
    print(err)
    sys.exit()
    