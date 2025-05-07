import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import string

df=pd.read_csv('hospital_data.csv')

#now storing complaints_summary in text file

# with open('complaints_summary.txt','w') as f:
#     for i in df['complaints_summary']:
#         f.write(i+'\n')

#finding average occupancy rate per ward
avg_occupancy_rate=df.groupby('ward')['occupancy_rate'].mean()
print("Average Occupancy Rate is: ",avg_occupancy_rate)

#identify the wards where occupancy rate exceeds 1 
print("Occupancy Rate Exceeds 1: \n",avg_occupancy_rate[avg_occupancy_rate>1])

occupancy_rates=np.array(df['occupancy_rate'])
print(occupancy_rates)

#calculating mean, sd
mean=np.mean(occupancy_rates)
sd=np.std(occupancy_rates)

print("Mean is: ",mean)
print("Standard Deviation is: ",sd)

#Identify wards 2 sd's above mean

overburdened_val=mean+2*sd
print(overburdened_val)

#now print those wards that have occupancy_rates>overburdened_val

overburdened_wards=avg_occupancy_rate[avg_occupancy_rate>overburdened_val]
print(overburdened_wards)

#Matplotlib visualization
max=avg_occupancy_rate.values.max()

#create a bar chart showing average occupancy rate per ward
# plt.figure(figsize=(10,6))
# plt.bar(avg_occupancy_rate.index,avg_occupancy_rate.values,label="Average Occupancy Rates",color=['red' if x==max else 'blue' for x in avg_occupancy_rate.values])
#Highlight the maximum value with different color
#Use condition coloring to highlight maximum value
# plt.title("Average Occupancy Rates per Ward")
# plt.xlabel("Ward")
# plt.ylabel("Average Occupancy Rate")
# plt.legend()
# plt.show()

#NLP Part

#Read the complaint text
with open('complaints_summary.txt','r') as f:
    complaints=f.read()


#Clean the text, convert to lowercase
complaints=complaints.lower()
#remove punctuations
complaints=complaints.translate(str.maketrans('','',string.punctuation))
#tokenize
tokens=word_tokenize(complaints)

stopwords=set(stopwords.words('english'))
filtered_tokens=[w for w in tokens if w not in stopwords]
# print(filtered_tokens)

#display the 5 most frequent mentioned complaint words
count=Counter(filtered_tokens)
print(count.most_common(5))
