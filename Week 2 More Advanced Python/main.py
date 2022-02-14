import pandas as pd

IMDB_CSV_FILE_NAME = "IMDb movies.csv"

imdb = pd.read_csv(IMDB_CSV_FILE_NAME)

# Exercise 1.1
bud = imdb[imdb.budget.str.contains('$', na=False, regex=False)].budget
# Exercise 1.2
imdb.budget = imdb.budget.apply(lambda x: str(x).strip('$'))
# Exercise 1.3
imdb.budget = pd.to_numeric(imdb.budget, errors='coerce')


# Exercise 2.1
for i in range(3):
    imdb["genre{0}".format(str(i))] = imdb.genre.apply(
        lambda x: "" if i >= len(str(x).split(',')) else str(x).split(',')[i])

# Exercise 3.1
imdb["numberOfActors"] = imdb.actors.apply(lambda x: len(str(x).split(',')))
# Exercise 3.2
imdb["mainActor"] = imdb.actors.apply(lambda x: str(x).split(',')[0])
