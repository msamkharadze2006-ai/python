import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# --- CHAPTER 1: JSON ---
# If loading string use loads
x = '{"name":"john", "mihso":"temo"}'
json_1 = json.loads(x)

# If you are loading a file use load
# Note: Check if "example.jsin" was a typo for ".json"
try:
    with open("example.json") as f:
        jason_2 = json.load(f)

    # json.dumps()
    with open("new_file.json", "w") as f_1:
        json_3 = json.dumps(jason_2, indent=4, separators=(";", "/"))
        f_1.write(json_3)
except FileNotFoundError:
    print("Note: example.json not found, skipping JSON file operations.")

# --- CHAPTER 2: MATPLOTLIB ---
x_points = [1, 2, 3]
y_points = [20, 30, 40]
x_points_1 = [10, 20, 30]
y_points_1 = [201, 301, 401]

plt.figure(figsize=(10, 8))

# Subplot 1
plt.subplot(2, 1, 1)
plt.plot(x_points, y_points, marker="o", mec="r", mfc="g", ls="--", lw=3, c="black")
font = {"family": "serif", "color": "blue", "size": 20}
plt.xlabel("days", fontdict=font)
plt.ylabel("income")
plt.title("Graph 1")
plt.grid(axis="both", c="black")

# Subplot 2
plt.subplot(2, 1, 2)
plt.plot(x_points_1, y_points_1, marker="o", mec="r", mfc="g", ls="--", lw=3, c="black")
plt.xlabel("days", fontdict=font)
plt.ylabel("income")
plt.title("Graph 2")
plt.grid(axis="both", c="black")

plt.suptitle("ME")
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

# Scatterplot
plt.figure()
c_2 = ["g", "r", "y"]
c_3 = [10, 20, 30]  # color map
plt.scatter(x_points, y_points, c=c_3, cmap="viridis", alpha=0.75)
plt.colorbar()
plt.title("Scatter Plot")
plt.show()

# --- CHAPTER 3: PANDAS & BOXPLOTS ---
try:
    df = pd.read_csv("australian_athlete_data.csv")

    # Boxplot 1: Random data
    plt.figure()
    data_to_plot = [np.random.normal(0, 1, 5000), np.random.normal(2, 2, 5000),
                    np.random.normal(-2, 2, 5000), np.random.normal(5, 5, 5000)]
    plt.boxplot(data_to_plot)  # Fixed the double nesting issue
    plt.title("Random Data Boxplot")
    plt.show()

    # Boxplot 2: Athletes data
    plt.figure()
    plt.boxplot([df.rcc, df.wt])
    plt.title("RCC vs Weight")
    plt.show()

    # Pandas Operations
    # 1. Query
    filtered_df = df.query("sport == 'B_Ball' & sex == 'm'")

    # 2. Unique sports
    unique_sports = df[["sport"]].drop_duplicates()

    # 3. Rename
    df = df.rename(columns={"sport": "SPORT"})

    # 4. Mutate (Assign)
    df = df.assign(rcc_div_wcc=df["rcc"] / df["wcc"])

    # 5. Groupby (Fixed the "grouby" typo)
    group_2 = df.groupby(["SPORT", "sex"])
    g_2 = group_2.agg({"ht": "median"})
    print("Grouped Median Height:")
    print(g_2)

except FileNotFoundError:
    print("Error: 'australian_athlete_data.csv' not found. Please check the file path.")