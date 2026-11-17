import os
import json
os.getcwd()
os.chdir("/Users/mishosamkharadze/Desktop/")
file_object = open("exam_json.json")

# TASK1:Decoding (loops, dictionaries, regexp, json)
# Locate your name and ‘code’ value in the uploaded “exam.json” file
# Remove characters that are part of your Neptun cod

# making function made more sense since it made easier to remove parts from code simpler
# because everything was part of same code, with seperation i got little confused so i went with this approach
def clean_text(text, chars_to_remove):

    forbidden = set(chars_to_remove.upper() + chars_to_remove.lower())
    return "".join([char for char in text if char not in forbidden])

with open('exam_json.json', 'r') as f:
    data = json.load(f)

students = data["Semester: "]["2025-26/II"]["course"]["python"]["students"]

target_name = "Samkharadze Mikheil"
neptun_chars = "HDTAPR"

for student in students:
    if student["name"] == target_name:
        original_name = student["name"]
        original_code = student["code"]

        new_code = clean_text(original_code, neptun_chars)

        print(f"Name: {original_name}")
        print(f"Original Code: {original_code}")
        print("-" * 20)
        print(f"Modified Code: {new_code}")
        break


# Sort the additional characters in descending order. Put letters first, prioritize lowercase
# # letters.

# here also i did not want to write variable like remaining_cahracters because it woudl be too
# specific and very singular for this case so instead i used my already used variable "new_code"
sorted_chars = sorted(new_code, key=lambda character: (
    not character.isalpha(),
    -ord(character.lower()),
    character.isupper()
))

print("".join(sorted_chars))

# Task 2: Analyze the “animals” dataset(pandas, plotting, string processing)

# Load the dataset
# How many observations and variables do we have in the data-set?
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
animals = pd.read_csv("animals_data.csv")

print("Observations:", animals.shape[0])
print("Variables:", animals.shape[1])


# Load dataset
animals = pd.read_csv("animals_data.csv")

# Visualize the 15 tallest animals’ height on a barplot. Use the maximum available values in
# m. Color them by conservation status
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('animals_data.csv')

df["Max Height (cm)"] = df["Height (cm)"].str.findall(r"(\d+\.?\d*)").str[-1]
df["Max Height (cm)"] = pd.to_numeric(df["Max Height (cm)"], errors="coerce")

df["Max Height (m)"] = df["Max Height (cm)"] / 100

top15_tallest = df.sort_values(by="Max Height (m)", ascending=False).head(15)

status_colors = {
    "Least Concern": "green",
    "Near Threatened": "lightgreen",
    "Vulnerable": "yellow",
    "Endangered": "orange",
    "Critically Endangered": "red",
    "Extinct": "black"
}


def map_status_to_color(status):
    status = str(status)
    if "Extinct" in status:
        return "black"
    return status_colors.get(status, "gray") # Default to gray for unknown statuses

colors = top15_tallest["Conservation Status"].apply(map_status_to_color)


plt.figure(figsize=(12, 7))

plt.bar(
    top15_tallest["Animal"],
    top15_tallest["Max Height (m)"],
    color=colors
)


plt.title("Top 15 Tallest Animals (Maximum Height in Meters)", fontsize=14)
plt.xlabel("Animal", fontsize=12)
plt.ylabel("Height (m)", fontsize=12)
plt.xticks(rotation=45, ha="right")
# plt.show()

# Which country/region is the most commonly mentioned? The categories are separated by ‘,’
# (comma).
df = pd.read_csv('animals_data.csv')

locations = df['Countries Found'].dropna().str.lower().str.split(',').explode().str.strip()

counts = locations.value_counts()

most_common_name = counts.idxmax()
most_common_count = counts.max()

print(f"Most commonly mentioned: {most_common_name}")
print(f"Number of mentions: {most_common_count}")

# Visualize the distribution of top speed of animals belonging to the biggest (most member)
# family

df = pd.read_csv('animals_data.csv')

biggest_family = df['Family'].value_counts().idxmax()

family_df = df[df['Family'] == biggest_family].copy()

family_df["Top Speed"] = family_df["Top Speed (km/h)"].str.extract(r"(\d+\.?\d*)$")
family_df["Top Speed"] = pd.to_numeric(family_df["Top Speed"], errors="coerce")

plt.figure(figsize=(6, 8))

speeds = family_df["Top Speed"].dropna()

plt.boxplot(speeds, labels=[biggest_family], patch_artist=True,
            boxprops=dict(facecolor='lightblue'))

plt.title(f"Top Speed Distribution for the {biggest_family} Family", fontsize=14)
plt.ylabel("Top Speed (km/h)", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()


# Create a new column “Lifespan_weeks” which contains the life span values in weeks
# 1. Extract the number. This regex picks the first number it sees

df["max_lifespan_value"] = df["Lifespan (years)"].str.extract(r"(\d+)").astype(float)

# 2.This is just incase scenario to avoid mistake with the data, i'll check in months and a
# # aslo its easier to operate with moths than years cuz there might be case where lifespan
# # is not exact year
is_month = df["Lifespan (years)"].str.contains("month", case=False, na=False)

# it translates moths to weeks and years to week
df["Lifespan_weeks"] = df["max_lifespan_value"] * 52
df.loc[is_month, "Lifespan_weeks"] = (df["max_lifespan_value"] / 12) * 52

# in the dataset there are many different values besides life psan like some for example say 12oct
# some result in NaN so i tried to mek column as big as i could with as much values i could

df["Lifespan_weeks"] = df["Lifespan_weeks"].fillna(0)

# 5. Check the result
print(df[["Animal", "Lifespan (years)", "Lifespan_weeks"]].head(20))


# TASK 3  Analyzing nucleotid sequences

# Which Prunus species have the highest AT content in their sequence? Process
# “Prunus_ITS.txt”

data = open('Prunus_ITS.txt').read().split('>')[1:]
results = {d.split('\n')[0]: d.upper().count('A') + d.upper().count('T') for d in data}

highest_species = max(results, key=results.get)
print(f"{highest_species}: {results[highest_species]}")




# Visualize the AT content for the top 5 species on a barplot
# it was bascially the same but with AT
entries = open('Prunus_ITS.txt').read().split('>')[1:]
species_data = []

for entry in entries:
    lines = entry.split('\n')
    name = lines[0].strip()

    sequence = "".join(lines[1:]).upper()
    at_count = sequence.count('A') + sequence.count('T')
    species_data.append((name, at_count))


top_5 = sorted(species_data, key=lambda x: x[1], reverse=True)[:5]
names = [x[0] for x in top_5]
counts = [x[1] for x in top_5]


plt.bar(names, counts, color='lightgreen', edgecolor='black')


plt.title("Top 5 Prunus Species by AT Count", fontsize=14)
plt.ylabel("Total AT Bases", fontsize=12)
plt.xlabel("Species", fontsize=12)

plt.ylim(min(counts) - 2, max(counts) + 2)

plt.tight_layout()
plt.show()