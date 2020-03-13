from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
#strg="Array is an  abstract data type which is used to store homogeneous data items in a contiguous memory location".lower()

def makeNGram(Ngram,strg):
    sa=[w for w in strg.split() if w not in ENGLISH_STOP_WORDS]
# =============================================================================
#     if Ngram == 1:
#         return sa
# =============================================================================
    i=0;
    ans=[];
    while( i+Ngram <= len(sa)):
        ans.append([])
        for j in range(Ngram):
            ans[i].append(sa[i+j]) 
        i+=1
    return ans