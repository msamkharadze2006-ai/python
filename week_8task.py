
# task 1
def chessboard(n):
    for i in range(n):
        for j in range(n):
            print("⬜" if (i + j) % 2 == 0 else "⬛", end=" ")
        print()  # move to next row

print(chessboard(8))

# task2
import pandas as pd
import os
os.getcwd()
os.chdir("/Users/mishosamkharadze/Desktop/")
file_object = open("australian_athlete_data.csv")

df = pd.read_csv("australian_athlete_data.csv")
# print(df)
# AVERAGE HEUGHT FEMALE B_BALL
female_nba = df[(df.sport == "B_Ball") & (df.sex ==  "f" )]
height = female_nba.loc[0:13,"ht"]
average = height.mean()
print(female_nba)
# print(average)

# Who weighs more on average? Male water polo players or male tennis players

weight = df.wt
overall_average = weight.mean()
print(weight.mean())

#

means = (df[(df["sex"] == "m") & (df["sport"].isin(["W_Polo", "Tennis"]))] \
  .groupby("sport")["wt"].mean())


print(means > weight.mean())
#Calculate the summary statistics for gymnasts

summary_gym= df[(df.sport == "Gym")]
summary  = summary_gym.describe()
print(summary)





