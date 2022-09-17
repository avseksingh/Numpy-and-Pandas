import numpy as np
import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

runs = {"Sachin": 100, "Pappu": 420, "Saubhagya": 1}
wickets = {"Sachin": 1, "Pappu": 420,"Saubhagya":0}
data = [runs, wickets]
index = ["Runs", "Wickets"]
df = pd.DataFrame(data, index)
print(df)
df.to_csv("F:\\Numpy-and-Pandas\\input.csv")  # F:\Numpy-and-Pandas
#df.to_csv("F:\\Numpy-and-Pandas\\input.xlsx")  # F:\Numpy-and-Pandas
# df.to_excel("h:\\csv\\scores.xlsx")
x = pd.read_csv("F:\\Numpy-and-Pandas\\input.csv", index_col=0)
print(x)
"""
x = pd.read_csv("F:\\Numpy-and-Pandas\\input.csv", index_col=0)
print(x)
x = pd.read_csv("F:\\Numpy-and-Pandas\\input.csv")
print(x)
x = pd.read_csv("F:\\Numpy-and-Pandas\\input.csv", index_col=0)
print(x)
x = pd.read_excel("F:\\Numpy-and-Pandas\\input.xlsx")
print(x)
x = pd.read_excel("F:\\Numpy-and-Pandas\\input.xlsx", index_col=0)
print(x)
"""