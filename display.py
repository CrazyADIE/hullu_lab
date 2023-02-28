import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('titles.csv')

new_df = df.groupby('release_year')['imdb_score'].mean()
new_df.plot(kind='bar')
plt.title('(avg.)imdb score each year')
plt.ylabel('imdb score')
plt.xlabel('release year')
plt.show()