import pandas as pd
pat_nme=["soumita","sneha","binu","pinu","sanu","riya","sonai","mouliki","mou","tusu"]
pat_id=[20,34,43,21,46,76,78,96,32,22]
ht=[5.5,5.6,6.1,6.1,6,5.9,5.8,5.8,5.8,9.1]
temp=[97.2,97.3,97.8,98,98.1,98.2,97.3,98,101,107]
dict={'patient_name':pat_nme,'patient_id':pat_id,'height':ht,'temparature':temp}
df=pd.DataFrame(dict)
print(df)
rows=len(df.axes[0])
print("number of rows:",rows)

import random
sample_list1=["headache","cold","fever"]
my_list1=[]
for i in range(0,rows):
    list1=random.choice(sample_list1)
    my_list1.append(list1)
print(my_list1)
dise=my_list1
print(dise)
new_dict1={'patient_name':pat_nme,'patient_id':pat_id,'height':ht,'temparature':temp,"disease":[]}
new_dict1["disease"]+=dise
df=pd.DataFrame(new_dict1)
print(df)
sample_list2=["BC Roy","TataMedical","SSKM"]
my_list2=[]
for i in range(0,rows):
    list2=random.choice(sample_list2)
    my_list2.append(list2)
print(my_list2)
hosp=my_list2
new_dict2={'patient_name':pat_nme,'patient_id':pat_id,'height':ht,'temparature':temp,'disease':dise,"Hospital":[]}
new_dict2["Hospital"]+=hosp
df=pd.DataFrame(new_dict2)
print(df)
cst=[20.0,1000.0,800.0,910.0,950.0,980.0,990.0,890.0,880.0,930.0]
my_list3=[]
for i in range(0,rows):
    list3=random.choice(cst)
    my_list3.append(list3)
print(my_list3)
Cost=my_list3
new_dict3={'patient_name':pat_nme,'patient_id':pat_id,'height':ht,'temparature':temp,'disease':dise,"Hospital":hosp,"cost":[]}
new_dict3["cost"]+=Cost
df=pd.DataFrame(new_dict3)
print(df)
##############----------------convert attribute of dataframe into list############----------
height_list= df['height'].tolist()
print(height_list)
cost_list=names = df['cost'].tolist()
print(cost_list)
temp_list=df['temparature'].tolist()
print(temp_list)
################-----------mean of HEIGHT--------################
sum=0
l=len(height_list)
for i in range(0,l):
    sum=sum+height_list[i]
    mean_height=sum/l
print("mean of height is:",mean_height)

####------------ median of HEIGHT----------------------###############
l = len(height_list)
height_list.sort()
  
if l % 2 == 0:
    median1 = height_list[l//2]
    median2 = height_list[l//2 - 1]
    median = (median1 + median2)/2
else:
    median = height_list[l//2]
print("Median of height is:", median)
#############----------------------MODE OF HEIGHT-----------#################
count=0
temp=0
index=0
for i in range(0,len(height_list)):
    temp=height_list.count(height_list[i])

    if(temp>count):
        count=temp
        index=i

mostFrequentnumber=height_list[index]
print("mode of height:",mostFrequentnumber)


###############------mean of COST-------######################
sum=0
l=len(cost_list)
for i in range(0,l):
    sum=sum+cost_list[i]
    mean_cost=sum/l
print("mean of cost is:",mean_cost)

#####################--------------median of COST-----------######################
l = len(cost_list)
cost_list.sort()
  
if l % 2 == 0:
    median1 = cost_list[l//2]
    median2 = cost_list[l//2 - 1]
    median = (median1 + median2)/2
else:
    median = cost_list[l//2]
print("Median of cost is:", median)

####################----------mode of COST-------------####################
count=0
temp=0
index=0
for i in range(0,len(cost_list)):
    temp=cost_list.count(cost_list[i])

    if(temp>count):
        count=temp
        index=i

mostFrequentnumber=cost_list[index]
print("mode of height:",mostFrequentnumber)


######################-------mean of TEMPARATURE-----------#########################
sum=0
l=len(temp_list)
for i in range(0,l):
    sum=sum+temp_list[i]
    mean_temp=sum/l
print("mean of temparature is:",mean_temp)

###########-----------------median Of TEMPARATURE------------------####################
l = len(temp_list)
temp_list.sort()
  
if l % 2 == 0:
    median1 = temp_list[l//2]
    median2 = temp_list[l//2 - 1]
    median = (median1 + median2)/2
else:
    median = temp_list[l//2]
print("Median of temparature is:", median)
##################------------MODE OF TEMPARATURE------------#################
count=0
temp=0
index=0
for i in range(0,len(temp_list)):
    temp=temp_list.count(temp_list[i])

    if(temp>count):
        count=temp
        index=i

mostFrequentnumber=temp_list[index]
print("mode of temparature:",mostFrequentnumber)









     










     


