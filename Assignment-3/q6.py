import pandas as pd

data_frame=pd.read_csv("employees.csv")
print(data_frame)

#Printing the shape of the dataset that is the number of rows and columns
print("Shape: ",data_frame.shape)

#Summary of the dataset that is the datatypes and non null indicators

print("Info: ",data_frame.info())

#Generating Descriptive Statistics

print("Description: ",data_frame.describe())

print(data_frame.iloc[:6],data_frame.iloc[-3:])

#Average Salary of the employees

print(data_frame['Salary'].mean())

#Total bonus paid to all the employees

print(data_frame['Bonus'].sum())

#Min of the employees Age

print(data_frame['Age'].min())

#Max of the rating

print(data_frame['Rating'].max())

#Sorting the dataframe according to the salary in descending order

sorted_df=data_frame.sort_values(by="Salary",ascending=False)
print(sorted_df)

#Adding a performance column by rating

data_frame["Performance"]=pd.cut(
    data_frame["Rating"],
    bins=[0,4.0,4.5,5.0],
    labels=["Average","Good","Excellent"]

)

#Finding the missing values in the dataframe
print(data_frame.isnull().sum())
data_frame["Bonus"]=data_frame["Bonus"].fillna(0)

#Rename the Employee_ID to ID

#Store the values in a new column, then delete the Employee_ID column and insert the ID column
# Method 1
# data_frame["ID"]=data_frame["Employee_ID"]
# data_frame.drop('Employee_ID',axis=1,inplace=True)
# print(data_frame)

#Method 2
data_frame.rename(columns={"Employee_ID":"ID"},inplace=True)
print(data_frame)

#Finding all the employees who have more than 5 years of experience
print(data_frame[data_frame["Years_of_Experience"]>5])

#Finding all the employees who are in the IT Department
print(data_frame[data_frame["Department"]=='IT'])

#Add a new Column Tax, which deducts 10% of the salary

data_frame["Tax"]=data_frame["Salary"]*(0.1)
print(data_frame)

#Lets save the modified data_frame in a new CSV file

data_frame.to_csv("new_employees.csv")
