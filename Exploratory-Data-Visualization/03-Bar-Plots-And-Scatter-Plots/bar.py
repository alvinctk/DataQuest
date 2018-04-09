import pandas as pd
import matplotlib.pyplot as plt
from numpy import arange

# Load Data
fandango = pd.read_csv("fandango_score_comparison.csv", encoding="Latin-1")
read = ["FILM", "RT_user_norm", "Metacritic_user_nom", "IMDB_norm", "Fandango_Ratingvalue", "Fandango_Stars"]
norm_reviews = fandango[read]

num_cols = ["RT_user_norm", "Metacritic_user_nom", "IMDB_norm", "Fandango_Ratingvalue", "Fandango_Stars"]

# Takes height from first row values
bar_heights = norm_reviews[num_cols].iloc[0].values

# Position of left side bars [0.75, 1.75, 2.75, 3.75, 4.75]
bar_positions = arange(5) + 0.75
width = 0.2

tick_positions = range(1,6)

fig, ax = plt.subplots()
ax.bar(bar_positions, bar_heights, width)
ax.set_xticklabels(labels=num_cols, rotation=90)
ax.set_xticks(ticks=tick_positions)

plt.title("Average User Rating For Avengers: Age of Ultron (2015)")
plt.xlabel("Rating Source")
plt.ylabel("Average Rating")


plt.show()
