import numpy as np
import pandas as pd

df = pd.read_excel(r"GeoFromPython.xls")

df.dropna()

mask = df[df["EnergySource"].isin(["Geothermal"]) == True]

mask = mask[mask["Change"].isin([0.0]) == False]

#mask["StateYear"] = mask["Year"]

#mask["StateYear"].apply(lambda x: x = str(x))

mask["StateYear"] = mask["State"] + mask["Year"].astype("str")

print(mask["StateYear"])

df["StateYear"] = df["State"] + df["Year"].astype("str")

df = df[df.StateYear.isin(mask["StateYear"])]

df = df.drop("StateYear", axis=1)

print(df)

df.to_excel("GeoFinal.xlsx")

means = df.groupby([df.State, df.EnergySource], as_index=False).Change.mean()

print(means)
