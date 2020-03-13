import sys
from scipy import spatial
from gensim.models import KeyedVectors
index = 0 

def main():
    path = "C:\\Users\\prashantDhirendra\\set II\\data\\models\\"
    try :
        print("loading the file...")
        model = KeyedVectors.load_word2vec_format(path+"GoogleNews-vectors-negative300.bin",binary=True)
        print(model)
    except:
        print('no word model used at '+ path+"GoogleNews-vectors-negative300.bin.gz")
        sys.exit();
    print(model.wv['hello'])
    

if __name__== "__main__": 
    main()
    print("this word is done by s")
 