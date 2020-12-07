import numpy as np
import pandas as pd

<<<<<<< HEAD
df = pd.read_excel(r"GeoFromPython.xls")

df.dropna()

mask = df[df["EnergySource"].isin(["Geothermal"]) == True]

mask = mask[mask["Change"].isin([0.0]) == False]

mask.to_excel("ForSQL.xlsx")

#df = df[(df["State"].isin(mask["State"])) & (df["Year"]).isin(mask["Year"])]

#key_names = ["State", "Year"]
#keys = [df["State"].unique, df["Year"].unique]

#df[df[key_names]==keys].to_excel("Check.xlsx")

#print(df)

df.to_excel("GeoFinal.xlsx")

means = df.groupby([df.State, df.EnergySource], as_index=False).Change.mean()

print(means)
=======
df = pd.read_excel(r"GeoForPython.xls")
print("Hello world!")
>>>>>>> 5018150bf9babdffb4a603387853eec512700378
