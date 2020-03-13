import pandas as pd
#pd.option_context('display.max_rows', None, 'display.max_columns', None)
df = pd.read_csv(r'C:\Users\prashantDhirendra\set II\data\workData\answerWiseSeprated\1.csv')
print(df.iloc[750].EssayText)