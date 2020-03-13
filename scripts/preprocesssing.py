from nltk.tokenize import word_tokenize
import pandas
import csv
import re
#import io 
#import codecs

path = ""

data = pandas.read_csv(r"C:\Users\prashantDhirendra\set II\data\workData\answerWiseSeprated\5.csv", 'if', error_bad_lines=False)
datas = csv.reader(data)
tokenData = word_tokenize(str(data))
#print(tokenData)
#print(str(cleaned_text))

cleaned_text2 = re.sub(r'[^\x00-\x7f]+','', str(tokenData))
#print(cleaned_text)

result = re.sub(r"[0-9]^[\w]+ ", '', str(cleaned_text2))
print(result)