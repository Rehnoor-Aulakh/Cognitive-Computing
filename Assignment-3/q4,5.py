import pandas as pd

#Q4
data_frame=pd.read_csv('Iris.csv')

#Q5, delete row 4 and delete column 3

data_frame.drop(4,axis=0,inplace=True)
data_frame.drop(data_frame.columns[3],axis=1,inplace=True)

print(data_frame)



