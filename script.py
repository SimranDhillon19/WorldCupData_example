import codecademylib3_seaborn
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("WorldCupMatches.csv")

df["Total Goals"] = df["Home Team Goals"] + df["Away Team Goals"]

print(df.head())

sns.set_style("whitegrid")
sns.set_context("talk", font_scale=1)

f, ax= plt.subplots(figsize=(19, 12))

ax = sns.barplot(data=df, x="Year", y="Total Goals")

ax.set_title("Average Number of Goals Scored In World Cup Matches By Year")

plt.show()

df_goals = pd.read_csv("goals.csv")
print(df_goals.head())

sns.set_context("talk", font_scale = 1.25)

f, ax2 = plt.subplots(figsize=(18, 10))

ax2 = sns.boxplot(data=df_goals, x="goals", y="year", palette = "GnBu")

ax2.set_title("Amount of Goals Scored in World Cups Over Time")

plt.show()


