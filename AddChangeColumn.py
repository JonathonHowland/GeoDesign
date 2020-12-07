#Add "Change" column and save to GeoFromPython.xls

import pandas as pd

#Input file for number of entries per year
Years = pd.read_excel(r"YearsForPython.xls")

#Data formatted for Python
df = pd.read_excel(r"GeoForPython.xls")

change = []
length = []
df = df.dropna()

#Remove "Type of Producer" (We don't care about it)
df = df.groupby(["Year", "State", "EnergySource"], as_index=False).Generation.sum()
df = df.sort_values(by=["Year","State"], ascending=[True, True])


#Check
print(df)

for i in range(len(df)):
    years = 0
    #There is no change for the first year
    if(df["Year"][i] == df["Year"][0]):
        print("{}, Initial year".format(i))
        change.append(0.0)
    else:
        #Never look more than two years back
        for j in range(len(Years)):
            if(df["Year"][i] == Years["Year"][j] and df["Year"][i] > 1991):
                for k in range(Years["Year"][j]-(Years["Year"][0]+1)):
                    years = years + Years["Count"][k]
        if(years > i):
            years = 0
        #Find the matching data point from a year earlier
        for j in range(years, i):
            if(df["Year"][j] == (df["Year"][i] - 1)):         
                if(df["State"][i] == df["State"][j]):
                    if(df["EnergySource"][i] == df["EnergySource"][j]):
                            print("{}, {}".format(years, i))
                            change.append((df["Generation"][i]-df["Generation"][j]))
    #If there is no matching data point, the change is zero
    if(len(change) != (i+1)):
        print("Error, {}".format(i))
        change.append(0.0)

#Append the changes to the dataset
Change = pd.Series(data=change)
df["Change"] = Change.values

#Check
print(df)

#Output file
df.to_excel('GeoFromPython.xls', index=False)
