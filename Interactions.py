#Code to create interaction terms from data
#in an Excel spreadsheet and save the new
#data with interactions to a new Excel file

#Only interactions with 4 or fewer terms
#are considered


import pandas as pd
import numpy as np

df = pd.read_excel(r'Project3Trimmed.xlsx')

df.fillna(0.5)
end = len(df.columns)


for i in range(3,end):
    for j in range(i+1, end):
        s1 = str(df.columns[i])
        s2 = str(df.columns[j])
        s = s1 + s2
        df.insert(i-3+end, s, df[s1]*df[s2])

newEnd = len(df.columns)

for i in range(3, end):
    for j in range(i+1, end):
        for k in range(j+1, end):
            s1 = str(df.columns[i])
            s2 = str(df.columns[j])
            s3 = str(df.columns[k])
            s = s1 + s2 + s3
            df.insert(i-3+newEnd, s, df[s1]*df[s2]*df[s3])

newEnd = len(df.columns)

for i in range(3, end):
    for j in range(i+1, end):
        for k in range(j+1, end):
            for l in range(k+1, end):
                s1 = str(df.columns[i])
                s2 = str(df.columns[j])
                s3 = str(df.columns[k])
                s4 = str(df.columns[l])
                s = s1 + s2 + s3 + s4
                df.insert(i-3+newEnd, s, df[s1]*df[s2]*df[s3])

print(df)

df.to_excel('Project3FromPython.xlsx', index=False)

#x = [1,2,3,4,5,6,7,8,9]

#xend = len(x)

#for i in range(0, xend):
 #   for j in range(i+1, xend):
  #      xi = x[i]*x[j]
   #     x.append(xi)

#for i in range(0, xend):
 #   xi = 1.0
  #  for j in range(i, xend):
   #     xi = xi*x[j]
    #    if(i != j):
     #       x.append(xi)

#for i in range(0,xend):
 #   for j in range(i+1,xend):
  #      for k in range(j+1, xend):
   #         for l in range(
    #        xi = x[i]*x[j]*x[k]
     #       x.append(xi)
#print(x)
