#importing module
import pandas as pd
from pandas import *
import numpy as np
from time import time
import matplotlib.pyplot as plt


#reading CSV file
#Removing header
#Giving column names
df = pd.read_csv("data\medical_transcriptions\mtsamples.csv", header=None, names=["serial no","description", "medical_specialty", "sample_name", "transcription", "keywords"])

#Converting Nan values to empty string values
df.fillna('', inplace=True)

#Sub-area 1
#Data preprocessing
#Converting medical_specialty column data to list
ms_list = df['medical_specialty'].tolist()


#Spliting the values and creating a list of value
my1_list = ms_list
res_1 = [item.split(',') for item in my1_list]
res_1_flat = [item for l in res_1 for item in l]
print(res_1_flat)

#Converting keywords column data to list
kw_list = df['keywords'].tolist()


#Spliting the values and creating a list of value
my2_list = kw_list
res_2 = [item.split(',') for item in my2_list]
res_2_flat = [item for l in res_2 for item in l]
print(res_2_flat)

#Converting sample_name column data to list
sn_list = df['sample_name'].tolist()

#Spliting the values and creating a list of values
my3_list = sn_list
res_3 = [item.split(',') for item in my3_list]
res_3_flat = [item for l in res_3 for item in l]
print(res_3_flat)

#Converting description column data to list
ds_list = df['description'].tolist()

#No need of preprocessing description 

#Converting transcription column data to list
ts_list = df['transcription'].tolist()

#No need of preprocessing transcription

#Sub-area 2
#Data analysis
#Preparing set of question and answering them using dataset

# Q.1.What is the most common medical specialty?
def most_frequent(res_1_flat):
    return max(set(res_1_flat), key = List.count)
List = res_1_flat
print('Most common medical_specialty is' + most_frequent(res_1_flat))
# Ans. Most common medical specialty is Surgery

# Q.2. What is the most common medical sample?
def most_frequent(res_3_flat):
    return max(set(res_3_flat), key = List.count)
List = res_3_flat
print('Most common sample_name is' + most_frequent(res_3_flat))
# Ans. Most common medical sample is Heart Catherterization 

# Q.3. What is the average length of the medical specialty?
t1_list = res_1_flat
res = sum(map(len, t1_list))/float(len(t1_list))
print("The Average length of medical specialty in list is : " + str(res))
# Ans. The Average length of medical specialty in list is : 16.0822

# Q.4. What is the average length of the keywords?
t2_list = res_2_flat
res = sum(map(len, t2_list))/float(len(t2_list))
print("The Average length of keywords in list is : " + str(res))
# Ans. The Average length of keywords in list is : 15.27

# Q.5. What is the average length of the sample name?
t3_list = res_3_flat
res = sum(map(len, t3_list))/float(len(t3_list))
print("The Average length of sample name in list is : " + str(res))
# Ans. The Average length of sample name in list is : 26.642

# Q.6. What is the average length of the description?
t4_list = ds_list
res = sum(map(len, t4_list))/float(len(t4_list))
print("The Average length of description in list is : " + str(res))
# Ans. The Average length of description in list is : 132.4164

# Q.7.What is the average length of the transcription?
t5_list = ts_list
res = sum(map(len, t5_list))/float(len(t5_list))
print("The Average length of transcription in list is : " + str(res))
# Ans. The Average length of transcription in list is : 3031.5612

# Q.8. What is total number of medical specialities?
my_list1 = res_1_flat
my_list1 = list(dict.fromkeys(my_list1))
size = len(my_list1)
print("Total number of medical_specialty is: " + str(size))
# Ans. Total number of medical_specialty is: 41

# Q.9. What is total number of medical samples?
my_list2 = res_3_flat
my_list2 = list(dict.fromkeys(my_list2))
size = len(my_list2)
print("Total number of sample_name is: " + str(size))
# Ans. Total number of sample_name is: 2410

# Q.10. What is total number of keywords?
my_list3 = res_2_flat
my_list3 = list(dict.fromkeys(my_list3))
size = len(my_list3)
print("Total number of keywords is: " + str(size))
# Ans. Total number of keywords is: 10445

# Q.11. How many times Autopsy medical specialty is used?
items = res_1_flat
count_a = items.count(' Autopsy')
print(f'Autopsy medical specialty is used {count_a=} times')
# Ans. Autopsy medical specialty is used 8 times.

# Q.12. How many times Bariatrics medical specialty is used?
items = res_1_flat
count_a = items.count(' Bariatrics')
print(f'Bariatrics medical specialty is used {count_a=} times')
# Ans. Bariatrics medical specialty is used 18 times.

# Q.13. How many times Lumbar Discogram sample is taken?
items = res_3_flat
count_a = items.count(' Lumbar Discogram ')
print(f'Lumbar Discogram sample is taken {count_a=} times')
# Ans. Lumbar Discogram sample is taken 5 times.


#Sub-area 3
#Data Visualization

# Histogram for visualize answers related to medical_specialty column
x1 = res_1_flat
plt.hist(x1, 50)
plt.title("medical_specialty")
plt.xlabel("medical_specialties")
plt.ylabel("Frequencies")
plt.xticks(rotation=90)
plt.show()

#Data visualization for medical specialty is done using histogram. Histogram shows relation b/w medical specialty
#and their frequencies. Beacuase of less no. of medical specialties, it is possible to show them in single histogram

#In case of sample name and other lists value, x axis elements is exceeding 1000+, so its not possible to show them in a single histogram.
#For this we can split list in sets of each 50 elements and and make multiple histograms
#For example
y = res_3_flat[1:50] #Histogram for first 50 elements in list
plt.hist(y, 50)
plt.title("medical sample")
plt.xlabel("sample name")
plt.ylabel("Frequencies")
plt.xticks(rotation=90)
plt.show()

#For the upcoming histograms there is no spliting of list but we can follow as above mentioned

# Histogram for visualize answers related to sample_name column
x2 = res_3_flat
plt.hist(x2, 50)
plt.title("medical sample")
plt.xlabel("sample name")
plt.ylabel("Frequencies")
plt.xticks(rotation=90)
plt.show()

# Histogram for visualize answers related to keywords column
x3 = res_2_flat
plt.hist(x3, 50)
plt.title("keywords")
plt.xlabel("keywords")
plt.ylabel("Frequencies")
plt.xticks(rotation=90)
plt.show()

# Histogram for visualize answers related to transcription column
x4 = ts_list
plt.hist(x4, 50)
plt.title("transcription")
plt.xlabel("transcription")
plt.ylabel("Frequencies")
plt.xticks(rotation=90)
plt.show()

# Histogram for visualize answers related to description column
x5 = ds_list
plt.hist(x5, 50)
plt.title("description")
plt.xlabel("description")
plt.ylabel("Frequencies")
plt.xticks(rotation=90)
plt.show()


