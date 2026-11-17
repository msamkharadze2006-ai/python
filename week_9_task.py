# import pandas as pd
# import os
# import matplotlib.pyplot as plt
# from pandas.plotting import boxplot
#
# os.getcwd()
# os.chdir("/Users/mishosamkharadze/Desktop/")
# file_object = open("animals_data.csv")
# # df = pd.read_csv("animals_data.csv")
# top_ten = df.sort_values(by="Weight (kg)", ascending= False).head(10)



# # Task 1: 10 heaviest animals' weight on a barplot
#
# df["Weight (kg)"] = df["Weight (kg)"].str.extract(r"(\d+\.?\d*)")
# df["Weight (kg)"] = pd.to_numeric(df["Weight (kg)"], errors="coerce")
# top10 = df.nlargest(10, "Weight (kg)")
# top10 = top10.sort_values(by="Weight (kg)")
# print(top10[["Animal", "Weight (kg)", "Color"]])
#
# c_1 = [
#     "gray",   # Narwhal
#     "Gray",  # White Rhinoceros
#     "Grey",  # Asian Elephant
#     "Grey",   # Great White Shark
#     "Grey",   # Great White Shark (duplicate)
#     "gray",   # African Elephant
#     "brown",  # Woolly Mammoth
#     "brown",  # Titanoboa
#     "black",   # Humpback Whale
#     "Gray"     # Sperm Whale ← HERE
# ]
#
# plt.bar(
#     top10["Animal"],
#     top10["Weight (kg)"],
#     color = c_1
# )
# plt.xticks(rotation=45, ha="right")  # key line
#
# plt.tight_layout()
# plt.show()
# print(top_ten[["Animal", "Weight (kg)"]])



# Task2 relationship between top speed and average speed




# df["Top Speed (km/h)"] = df["Top Speed (km/h)"].str.extract(r"(\d+\.?\d*)")
# df["Average Speed"] = df["Average Speed (km/h)"].str.extract(r"(\d+\.?\d*)")
#
# df["Top Speed (km/h)"] = pd.to_numeric(df["Top Speed (km/h)"], errors="coerce")
# df["Average Speed (km/h)"] = pd.to_numeric(df["Average Speed (km/h)"], errors="coerce")
#
#
# df = df.dropna(subset=["Top Speed (km/h)", "Average Speed (km/h)"])
#
# diet_colors = {
#     "carnivore": "red",
#     "herbivore": "green",
#     "omnivore": "brown",
#     "insectivore":"white",
#     "scavenger":"blue",
#     "nectar" : "orange",
#     "filter feeder":"cyan"
#
# }
#
# df["Diet"] = df["Diet"].str.lower().str.strip()
#
# colors = df["Diet"].map(diet_colors)
#
# colors = colors.fillna("gray")
#
# plt.figure(figsize=(8,6))
#
# plt.scatter(
#     df["Average Speed (km/h)"],
#     df["Top Speed (km/h)"],
#     c=colors,
#     alpha=0.7
# )
#
# plt.xlabel("Average Speed (km/h)")
# plt.ylabel("Top Speed (km/h)")
# plt.title("Top Speed vs Average Speed by Diet")
#
# plt.show()



# Task 3: Which animal is the most commonly mentioned predator

# predators = df["Predators"].dropna().str.lower()
#
# # split multiple predators
# predators = predators.str.split(",")
# predators = predators.explode()
#
# # remove spaces
# predators = predators.str.strip()
#
# # remove useless entries
# predators = predators[predators != "none"]
#
# # count
# counts = predators.value_counts()
#
# # get most common
# most_common = counts.idxmax()
# count = counts.max()
#
# print(most_common, count)

# Task4:
# df["Gestation Period (days)"] = df["Gestation Period (days)"].str.extract(r"(\d+\.?\d*)")
# df["Gestation Period (days)"] = pd.to_numeric(df["Gestation Period (days)"], errors="coerce")
# groups = df.groupby("Family")["Gestation Period (days)"].apply(list)

# plt.figure(figsize=(12,6))
# r_1 = df["Gestation Period (days)"]
# r_2 = df["Family"]
# plt.boxplot(groups, labels=groups.index)
# plt.show()


# In which habitat do we have the most 'Critically Endangered' species?

# x = df[df["Conservation Status"] == "Critically Endangered"]["Habitat"].value_counts().idxmax()
# print(x)