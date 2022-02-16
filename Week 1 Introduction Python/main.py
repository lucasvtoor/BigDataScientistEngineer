import pandas as pd
import plotly.io as plot

AMOUNT_OF_DTYPES = 22
IMDB_CSV_FILE_NAME = 'IMDb movies.csv'

# 1. Read in the file “IMDB movies.csv”
imdb = pd.read_csv(IMDB_CSV_FILE_NAME,sep=',')

# 2.	Check you are using the right separator
print(len(imdb.dtypes) == AMOUNT_OF_DTYPES)

# 3.a amount of rows
print(len(imdb))

# 3.b amount of columns
print(len(imdb.columns))

# 3.c	What is the mean of the duration of all movies?
print(imdb["duration"].mean())

# 4.d	How many movies are there in the dataframe where country =’USA’?
print(len(imdb[imdb["country"] == "USA"]))

# This might be neater by using a variable
usa_filter = imdb["country"] == "USA"
amount = len(imdb[usa_filter])

# 3.e	What is the longest title , measured in number of characters?
pd.options.display.max_colwidth = 200
print(imdb.sort_values(by="title", key=lambda title: title.str.len(), ascending=False).head(1).title)
pd.options.display.max_colwidth = 50

# 4.	Plot a chart with the number of movies for each year.

data = [dict(
    type='bar',
    x=imdb["year"],
    y=imdb["year"],
    transforms=[
        dict(
            type='aggregate',
            groups=imdb['year'],
            aggregations=[
                dict(
                    target='y', func='count', enabled=True
                )
            ]
        )
    ]
)]
fig_dict = dict(data=data)

plot.show(fig_dict, validate=False)
