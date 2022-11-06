import pandas as pd

df = pd.read_csv('gameDB.csv', sep='\t')
df.drop(columns=['originalTitle', 'sortingTitle', 'summary', 'myRating', 'isHidden', 'backgroundImage', 'squareIcon', 'verticalCover'],
        inplace=True)
# random_index = df.sample(n=1).index[0]
print(df.sample(n=1).to_string(index=False))
