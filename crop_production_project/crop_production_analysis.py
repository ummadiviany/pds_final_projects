# SAMPLE QUESTIONS:
#Which `crop` has the `highest production` in the country?
#What are the major `states` where `rice` is grown?
#What is the `average cost of cultivation` of `rice` in the country?
#What are seasons where `Sunflower` is grown? (data availabe in `datafile_5.csv`)
#What is average cost of production for `Paddy`, `Wheat` and `Maize`?

import os

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import ticker

df1 = pd.read_csv(os.path.abspath('data/crop_production/datafile_1.csv').replace('\\','/'))
df2 = pd.read_csv(os.path.abspath('data/crop_production/datafile_2.csv').replace('\\','/'))
df3 = pd.read_csv(os.path.abspath('data/crop_production/datafile_3.csv').replace('\\','/'))
df4 = pd.read_csv(os.path.abspath('data/crop_production/datafile_4.csv').replace('\\','/'))
df5 = pd.read_csv(os.path.abspath('data/crop_production/datafile_5.csv').replace('\\','/'))

#---------------------------------------------------------------------------------------------------------------
# Q1. Which crop has the highest production in the country?
#---------------------------------------------------------------------------------------------------------------
def Question1():
    crop_list = df1['Crop'].to_list()
    crop_yield = df1['Yield (Quintal/ Hectare) '].to_list()
    crop_u = df1['Crop'].unique()
    crop_y = []
    for i in range(len(crop_u)):
        c = 0
        for j in range(len(crop_list)):
            if crop_u[i] == crop_list[j]:
                c += crop_yield[j]
        crop_y.append(c)
    crop_y = [round(crop_y[i],2) for i in range(len(crop_y))]
    max_index = pd.Series(crop_y).idxmax()
    print (crop_u[max_index])

    # Bar Graph
    plt.figure(figsize=(10 ,5))
    graph = plt.bar(crop_u, crop_y, width = 0.4)
    plt.xlabel('Crops')
    plt.ylabel('Yield (Quintal/hectare)')
    plt.xticks(rotation = 45)
    plt.title('Yield of Various Crops')
    for i in range(len(crop_u)):
        plt.text(i , crop_y[i], crop_y[i], ha = 'center' , va = 'bottom')
    plt.show()

#---------------------------------------------------------------------------------------------------------------
# Q2. What are the major `states` where `rice` is grown?
#---------------------------------------------------------------------------------------------------------------

def Question2():
    paddy = df3[df3['Crop']== 'Paddy'].drop(index = 1).drop(columns = 'Season/ duration in days')
    
    paddy_i= paddy.reset_index()
    print (paddy_i.drop(columns='index'))



#---------------------------------------------------------------------------------------------------------------
# Q3. What is the `average cost of cultivation` of `rice` in the country?
#---------------------------------------------------------------------------------------------------------------

def Question3():
    #paddy_total = df1.groupby('Crop').get_group('PADDY')
    paddy_total = df1[df1['Crop'] == 'PADDY'].drop(columns=['Cost of Production (`/Quintal) C2','Yield (Quintal/ Hectare) ']).reset_index().drop(columns= 'index')
    print (paddy_total,'\n')
    AVG1 = paddy_total['Cost of Cultivation (`/Hectare) A2+FL'].mean()
    AVG2 = paddy_total['Cost of Cultivation (`/Hectare) C2'].mean()
    print (f'-> Average cost of prodcution for (`/Hectare) A2+FL is Rs.{round(AVG1,2)} \n-> Average cost of production for (`/Hectare) C2 is Rs.{round(AVG2,2)}')

#---------------------------------------------------------------------------------------------------------------
# Q4. What are seasons where `Sunflower` is grown?
#---------------------------------------------------------------------------------------------------------------

def Question4():
    sunflower = df5[['Particulars','Frequency']]
    sunflower_rows = sunflower[sunflower['Particulars'].str.contains('Sunflower')] # It shows all the rows with sunflower present in it 
    print (sunflower_rows.reset_index().drop(columns='index'))

#---------------------------------------------------------------------------------------------------------------
# Q5. What is average cost of production for `Paddy`, `Wheat` and `Maize`?
#---------------------------------------------------------------------------------------------------------------

def Question5():
    production = df1[['Crop','Cost of Production (`/Quintal) C2']]
    paddy = production[production['Crop']=='PADDY']
    paddy_mean = round(paddy['Cost of Production (`/Quintal) C2'].mean(),2)
    wheat = production[production['Crop']=='WHEAT']
    wheat_mean = round(wheat['Cost of Production (`/Quintal) C2'].mean(),2)
    maize = production[production['Crop']=='MAIZE']
    maize_mean = round(maize['Cost of Production (`/Quintal) C2'].mean(),2)

    print("1. Average cost of production of paddy is Rs.", paddy_mean)
    print("2. Average cost of production of wheat is Rs,", wheat_mean)
    print("3. Average cost of production of maize is Rs.", maize_mean)

#---------------------------------------------------------------------------------------------------------------
# Q6. Which is the highest cotton producing state in the country?
#---------------------------------------------------------------------------------------------------------------

def Question6():
    cotton = df1[df1['Crop']=='COTTON'].drop(columns=['Cost of Cultivation (`/Hectare) A2+FL','Cost of Cultivation (`/Hectare) C2','Cost of Production (`/Quintal) C2']).reset_index().drop(columns= 'index')
    max_index = cotton['Yield (Quintal/ Hectare) '].idxmax()

    print (f"The maximum cotton producing state in the country is {cotton['State'][max_index]}")

#---------------------------------------------------------------------------------------------------------------
# Q7. In the year 2007-2008 which crop has the highest productivity and what was the corresponding area and yield at the same time?
#---------------------------------------------------------------------------------------------------------------

def Question7():
    high_prod_idx = df2['Production 2007-08'].idxmax()

    print (f"The crop having the highest productivity during the period of 2007-2008 is :{df2['Crop             '][high_prod_idx]}")
    print (f"The maximum production is : {df2['Production 2007-08'][high_prod_idx]}")
    print (f"The area covered by the crop during that period is : {df2['Area 2007-08'][high_prod_idx]}")
    print (f"The yield that was obtained during that time interval : {df2['Yield 2007-08'][high_prod_idx]}")


#---------------------------------------------------------------------------------------------------------------
# Q8. In the year 2009-2010 show the percentage distribution of all the crops based on the area covered by each of the crops
#---------------------------------------------------------------------------------------------------------------

def Question8():
    area_dataframe = df2[['Area 2009-10']]
    area = df2['Area 2009-10']
    area_list = area.to_list()
    #print (area_list)
    sum_area = round(area.sum(),2)
    percentage_list = []
    #print (sum_area)
    for i in range(len(area)):
        frac = round(area_list[i]/sum_area,4)*100
        percentage_list.append(frac)
    area_dataframe.insert(loc = 1,column='Percentage_distribution_2009-10 (%)',value= percentage_list)
    
    print (area_dataframe)

#---------------------------------------------------------------------------------------------------------------
# Q9. What is the yield distributtion of paddy in India?
#---------------------------------------------------------------------------------------------------------------

def Question9():
    paddy =df1[df1['Crop'] == 'PADDY']
    paddy_yield = paddy[['Crop','State','Yield (Quintal/ Hectare) ']].reset_index().drop(columns= 'index')
    total_yield_paddy = paddy_yield['Yield (Quintal/ Hectare) '].sum()
    percent = []
    
    paddy_yield_list = paddy_yield['Yield (Quintal/ Hectare) '].to_list()
    for i in range(len(paddy_yield_list)):
        percent.append(round(paddy_yield_list[i]/total_yield_paddy,5)*100)
    
    paddy_yield['Percentage Yield'] = percent

    print (paddy_yield)
    # Pie plot
    explode = [0.1,0.1,0.1,0.1,0.1]
    plt.title("Paddy Yield Distribution in India", loc = 'center', fontdict={'fontsize':15})
    plt.pie(paddy_yield_list, labels = paddy_yield['State'].to_list(), explode = explode, autopct='%1.1f%%', shadow=True, wedgeprops={'edgecolor':'black'})
    plt.show()

#---------------------------------------------------------------------------------------------------------------
# Q10. Which state has the highest `cost of cultivation` for cotton ?
#---------------------------------------------------------------------------------------------------------------

def Question10():
    cost = df1[df1['Crop'] == 'COTTON']
    cost_cultivation = cost[['Crop','State','Cost of Cultivation (`/Hectare) A2+FL','Cost of Cultivation (`/Hectare) C2']].reset_index().drop(columns='index')
    cost_cultivation['Total cultivation cost'] = cost_cultivation['Cost of Cultivation (`/Hectare) A2+FL'] + cost_cultivation['Cost of Cultivation (`/Hectare) C2']
    high_index = cost_cultivation['Total cultivation cost'].idxmax()
    print (f"The state having the highest cost of cultivation of cotton is - {cost_cultivation['State'][high_index]}"+"\n\n"+f"The maximum cost of cultivation is Rs. {cost_cultivation['Total cultivation cost'][high_index]}")

#---------------------------------------------------------------------------------------------------------------
# Q11. Which Kharif crop has the highest yield in the year 2011 ?
#---------------------------------------------------------------------------------------------------------------

def Question11():
    kharif = df5[['Particulars',' 3-2011']]
    kharif_rows = kharif[kharif['Particulars'].str.contains('Kharif')].reset_index().drop(columns='index')
    highest_index = kharif_rows [' 3-2011'].idxmax()
    print (f"The kharif crop with the highest yield in the year 2011 is \n '{kharif_rows['Particulars'][highest_index]}'"+"\n\n"+f"The yield of the kharif crop is {kharif_rows[' 3-2011'][highest_index]} ton mn")

#---------------------------------------------------------------------------------------------------------------
# Q12. Which crops are grown in Orissa and West Bengal both ?
#---------------------------------------------------------------------------------------------------------------

def Question12():
    state = df3.dropna(subset= ['Recommended Zone'])
    state_specific = state[state['Recommended Zone'].str.contains('Orissa','West Bengal')].reset_index().drop(columns=['index','Season/ duration in days'])
    print (state_specific)

#---------------------------------------------------------------------------------------------------------------
# Q13. Prepare a comparative distribution of overall crop production for year 2009 denoting total yield
#---------------------------------------------------------------------------------------------------------------

def Question13():
    crop = df2[['Crop             ','Yield 2008-09','Yield 2009-10']]
    print (crop)

    # Horizontal bar plot 1
    fig, ax = plt.subplots(figsize= (16,9))
    ax.barh(crop['Crop             '], crop['Yield 2008-09'], color = 'maroon')
    plt.xlabel("Yield")
    plt.ylabel("Crops")
    ax.yaxis.set_major_locator(ticker.FixedLocator([i for i in range(55)]))
    ax.set_yticklabels(crop['Crop             '].to_list(),fontsize = 5, rotation = 0)
    plt.title("Yield for 2008-2009")

    plt.show()

    # Horizontal bar plot 2

    fig, bx = plt.subplots(figsize= (16,9))
    bx.barh(crop['Crop             '], crop['Yield 2009-10'], color = 'blue')
    plt.xlabel("Yield")
    plt.ylabel("Crops")
    bx.yaxis.set_major_locator(ticker.FixedLocator([i for i in range(55)]))
    bx.set_yticklabels(crop['Crop             '].to_list(),fontsize = 5, rotation = 0)
    plt.title("Yield for 2009-2010")

    plt.show()

#---------------------------------------------------------------------------------------------------------------
# Q14. List the different varieties of paddy and wheat grown in India
#---------------------------------------------------------------------------------------------------------------

def Question14():
    paddy_variety = df3[df3['Crop']=='Paddy']
    print ("varieties of paddy are :-\n\n",paddy_variety[['Variety']],"\n")
    wheat_variety = df3[df3['Crop'] == 'Wheat'].reset_index().drop(columns='index')
    print ("Varieties of Wheat are :-\n\n",wheat_variety[['Variety']])

#---------------------------------------------------------------------------------------------------------------
# Q15. Compare the production of rice, wheat, maize and bajra from 2006 to 2011
#---------------------------------------------------------------------------------------------------------------

def Question15():
   compare = df2[df2['Crop             '].isin(['Rice','Wheat','Maize','Bajra'])]
   compare_production = compare[['Crop             ','Production 2006-07','Production 2007-08','Production 2008-09','Production 2009-10','Production 2010-11']].reset_index().drop(columns='index')
   x = ['Production 2006-07','Production 2007-08','Production 2008-09','Production 2009-10','Production 2010-11']
   compare_transpose = compare_production.transpose().drop(index = 'Crop             ')
   
   rice =np.array( compare_transpose[0].to_list())
   wheat = np.array(compare_transpose[1].to_list())
   maize = np.array(compare_transpose[2].to_list())
   bajra = np.array(compare_transpose[3].to_list())
   # plot bar
   
   width = 0.2
   plt.figure(figsize=(10,6))
   plt.bar(x,rice,color = 'r')
   plt.bar(x,wheat, bottom=rice,color = 'b')
   plt.bar(x,maize,bottom=rice+wheat,color = 'y')
   plt.bar(x,bajra,bottom=rice+wheat+maize,color = 'g')
   plt.xlabel("Years")
   plt.ylabel("Production")
   plt.legend(['Rice','Wheat','Maize','Bajra'])
   plt.title('Comparison between the Production in the Years')
   
   plt.show()


   


# The Questioning Part and the outer Frame Work of the Project
t = 0
for i in range(125):
    print("-",end="")
print()
print ('\33[1m' "Welcome to Agriculture Crop Production Analysis".center(125))
for i in range(125):
    print("-",end="")
print("\n\n"'\33[m')
print('\33[4m'"-: Questions available to be answered :-", end="\n\n")
print("--Type just the question number to get the corresponding answer--\n\n")
print ('\33[m'"1. Which crop has the highest production in the country?\n2. What are the major `states` where `rice` is grown?")
print ("3. What is the `average cost of cultivation` of `rice` in the country?\n4. What are the seasons where `Sunflower` is grown")
print ("5. What is average cost of production for `Paddy`, `Wheat` and `Maize`?\n6. Which is the highest cotton producing state in the country?")
print ("7. In the year 2007-2008 which crop has the highest productivity and what was the corresponding area and yield at the same time?")
print ("8. In the year 2009-2010 show the percentage distribution of all the crops based on the area covered by each of the crops")
print ("9. What is the yield distributtion of paddy in India?\n10. Which state has the highest `cost of cultivation` for cotton ?")
print ("11. Which Kharif crop has the highest yield in the year 2011 ?\n12. Which crops are grown in Orissa and West Bengal both ?")
print ("13. Prepare a comparative distribution of overall crop production for year 2009 denoting total yield\n14. List the different varieties of paddy and wheat grown in India")
print ("15. Compare the production of rice, wheat, maize and bajra from 2006 to 2011")
print ("Press 0 to terminate and exit\n\n")
c = True
while (c == True):
    qno = int(input("Enter the question number you want to get answered - "))
    if (qno == 1):
        print ("-: Answer to the question :- \n\n")
        Question1()
    elif (qno == 2):
        print ("-: Answer to the question :- \n\n")
        Question2()
    elif (qno == 3):
        print ("-: Answer to the question :- \n\n")
        Question3()
    elif (qno == 4):
        print ("-: Answer to the question :- \n\n")
        Question4()
    elif (qno == 5):
        print ("-: Answer to the question :- \n\n")
        Question5()
    elif (qno == 6):
        print ("-: Answer to the question :- \n\n")
        Question6()
    elif (qno == 7):
        print ("-: Answer to the question :- \n\n")
        Question7()
    elif (qno == 8):
        print ("-: Answer to the question :- \n\n")
        Question8()
    elif (qno == 9):
        print ("-: Answer to the question :- \n\n")
        Question9()
    elif (qno == 10):
        print ("-: Answer to the question :- \n\n")
        Question10()
    elif (qno == 11):
        print ("-: Answer to the question :- \n\n")
        Question11()
    elif (qno == 12):
        print ("-: Answer to the question :- \n\n")
        Question12()
    elif (qno == 13):
        print ("-: Answer to the question :- \n\n")
        Question13()
    elif (qno == 14):
        print ("-: Answer to the question :- \n\n")
        Question14()
    elif (qno == 15):
        print ("-: Answer to the question :- \n\n")
        Question15()
    
    elif(qno == 0):
        print ("\n\nThank you for your time........\nWish you enjoyed the analysis")
        break
    else:
        print ("You have entered an incorrect choice\n\n")
    while (t<3):
        s = input("Do you wish to continue ?\n\nIf yes type 'Y' else type 'N' ")
        if s == 'Y' or s == 'y':
            break
        elif s == 'N' or s == 'n':
            break
        else:
            print ("!!!..You have entered an inappropriate character, please check the character you have typed..!!!")
            t+=1
    if s == 'Y' or s == 'y':
        continue
    if s == 'N' or s == 'n':
        print ("Thank you for your time........\nWish you enjoyed the analysis")
        break
    if t == 3:
        print ("You have entered invalid input too many times, hence the program has terminated.....Sorry for the inconvenience..!!!")
        break
    