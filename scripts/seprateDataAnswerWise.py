## make tsv to csv file
#import header file
import pandas as pd
inPath = r'C:\Users\prashantDhirendra\set II\data\rawdata\train.tsv'
outPath = r'C:\Users\prashantDhirendra\set II\data\workData\answerWiseSeprated\\'
#load dataframe
df = pd.read_csv(inPath, sep='\t')

#save answers in different csv file
for i in range(10):
    df[df.EssaySet== i+1].to_csv(outPath+str(i+1)+".csv",encoding='utf-8',index=False)