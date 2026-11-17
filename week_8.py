# import numpy as np
#
# # 1D
# arr = np.array([1, 2, 3])
# print(arr)
# # 2D
#
# arr_2 = np.array([[1,2,3],[4,5,6]])
#
# arr_2_2= np.array([[1,2,3], [ "misho", "temo","2" ]])
# print(arr_2)
# # arr_2[0:2] first(0) is row nad second(2) is column
#
# # 3D
#
# arr_3 = np.array([[[1,2,3],[4,5,6]], [7,8,9], [10,11,12]])
#
# arr_4  = np.array([1,2,3], ndmin= 3) #ndmin can give dimensions to a matrix
#
#
#
# # arr = np.array(["misho", "temo"])
# # print(arr)
#
#
# # print(arr_3)
#
# # dtype (attribute) : returns data type of the array
#
# arr_2.dtype
#
# # shape that returns a tuple with each index having the number of corresponding elements
#
# arr_2.shape
#
# # reshape
# arr = np.array(range(12))
# arr.reshape(3,4)
#
# # flatten
# m_1.reshape(-1)
# arr_3.reshape(-1)
#
# #sort
#
# np.sort(arr_3)
#
# # iteration
#
# for i in arr_2:
#     print(i)
#
# for i in arr_3:
#     for j in i:
#         print(j)
#
# #element-wise execution
#
# arr + 5
#
# arr_2 + 2
#
# # logical slicing
#
# arr[arr>5]
#
#
# np.where(arr > 5)
#
# # Chapter 2 : Panda


import pandas as pd

df = pd.read_csv("australian_athlete_data.csv")
print(df)
# create data.frames

mydata = {
    "cars" :[ "BMW", "Volva", "Ford"],
    "passings" : [3,7,2]
}

df_2 = pd.DataFrame(mydata)

# create series(columns)
col_1 = pd.Series(["banana", "apple"])
# col_1[:]

# col_1[col_1 == "apple"]

#loc, iloc attribute

df.loc[0:2]
df_2.iloc[0:2]

df_2 = df.loc[0:2]

df_2.index = ["banana" , "bannana", "apple"]

df.loc[0:2]

df_2 = [["rcc", "wcc"]]
df_2.rcc
df_2.rcc[0:2]

# filter rows based on logical conditions

df_3 = df[df.rcc > 4]

df[df.sport == "B_Ball"]

# df[(df.sport == "B_Ball")|(df.sport == "W_Polo")]

# isin() mehtod for filtering
# df[df["sport"].isin(["B_Ball", "W_Polo"])]

# head mehtod
# df.head()
# tail
# df.tail()
# infot and describe methods

# df.info()
# summary_stat = df.describe()


# Handling missing values : dropna() and fillna() methods

# df.rcc[0] = None
#
# df_4 = df.dropna()
# df_5 = df.fillna(5)

# Dataframe.sort_index() sorts by an axis and Daraframe.sort_Values(bys"coname") sorts by value

df.sort_index(axis = 0)
df_5 = df.sort_va;ues(by = "sport", ascending = False)
