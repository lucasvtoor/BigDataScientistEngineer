import pandas as pd

# more ugly df= pd.read_csv('IMDb movies.csv')
df = pd.read_csv('IMDb movies.csv', sep=',')

df.head(10)
