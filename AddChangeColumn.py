import numpy as np
import pandas as pd

def MakeChangeCol(df):
    for i in range(len(df)):
        for j in range(i+1, len(df)):
            year = int(df["YEAR"][i])
            if(df[str(year)][j] == df[str(year+1)][i] & df["ENERGY SOURCE"][i] == df["ENERGY SOURCE"]):
                

df = pd.read_excel(r"GeoForPython.xls")
