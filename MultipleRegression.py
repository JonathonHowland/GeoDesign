#Code to run iterative multiple regressions, with each iteration
#removing a variable with a high p-value or a very low
#(approximately 0) coefficient

#Output and input file names can be edited as necessary
#with no other alterations to the code

#Excel files must have only the relevant data
#No extra information in other cells

#Null values are replaced with 0.5

import pandas as pd
import numpy as np
from sklearn import linear_model
import statsmodels.api as sm

df = pd.read_excel(r'Project3FromPython.xlsx')

file = open("DDProject3OutputPoly.txt", "a")

df = df.fillna(0.5)

end = len(df.columns)

cols = []
Y = df['Weight']
    
for i in range(3, end):
    s = str(df.columns[i])
    cols.append(s)

max = 1.0

while(max > 0.05):
        
    X = df[cols]
        
    X = sm.add_constant(X)

    model = sm.OLS(Y,X).fit()

    print_model = model.summary()
    print(print_model, file=file)


    check = model.summary2().tables[1]['Coef.']
    checkSum = 0
    for i in range(0, len(check.values)):
        if (abs(check.values[i]) <  0.01):
            checkSum = checkSum+1
            del df[cols[i-1]]
            cols.pop(i-1)
            break

    if(checkSum != 0):
        del X
    
    if(checkSum == 0): 
        pValues = model.summary2().tables[1]['P>|t|']
        
        max = 0
        maxi = 0
        
        for i in range(0, len(pValues.values)):
            if (max<pValues.values[i]):        
                max = pValues.values[i]
                maxi = i
            
        if(max > 0.05):
            del df[cols[maxi-1]]
            cols.pop(maxi-1)
            del X

        print(cols)

        print(df)


df.to_excel('Project3Trimmed.xlsx', index=False)

#print("\n \n \n Adding interaction terms... \n \n \n", file=file)
