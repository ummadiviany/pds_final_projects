# Crop Production Analysis
### Final Project for CS60013 : Programming and Data Structures
---

> ## **Introduction**

This project aims to analyse the crop production data from 2006 to 2011 from all the states of India. The datas were provided in CSV format, located in the `data/crop_production/` directory. In order to analyze the data several approaches were considered on the basis of *Python Coding* and with the application of several libraries namely as : - 

1. `Pandas`
2. `Matplotlib`
3. `OS`
4. `Numpy`

---
> ## **Data**

In this project the CSV files that were provided, consisted of various types of `parameters` like Crops, Productions, Yield, locations, seasons. The purpose of the project to analyze the data in such a manner so as to create a relation between these datas for better visualization. Hence with the help of these libraries we managed to plot graphs, and plot dataframes on the basis of questions that were created on our own.

---
> ## **Questions and Answers**

1. ***Which crop has the highest production in the country?***
    - `datafile_1.csv` was considered and the dataframe was formed based on `yield` column and a *bar_graph* was plotted.

2. ***What are the major `states` where `rice` is grown?***
    - `datafile_3.csv` was considered and dataframe was formed with states in which paddy was grown by dropping all the unwanted columns and datas.

3. ***What is the `average cost of cultivation` of `rice` in the country?***
    - `datafile_1.csv` was considered and average cost of cultivation columns and corresponding paddy rows were considered.

4.  ***What are seasons where `Sunflower` is grown?***
    - `datafile_5.csv` was considered and *'Frequency'* column and *'Particulars'* column was chosen based on sunflowe in the rows

5. ***What is average cost of production for `Paddy`, `Wheat` and `Maize`?***
    - Form `datafile_1.csv` the rows based on these crops were considerd and the corresponding average production costs were calculated after dropping the rest of the unwanted columns

6. ***Which is the highest cotton producing state in the country?***
    - From `datafile_1.csv` the data was obtained and displayed

7. ***In the year 2007-2008 which crop has the highest productivity and what was the corresponding area and yield at the same time?***
    - `datafile_2.csv` was taken under consideration and for the required datas, the corresponding colums were selected and the rest were dropped using `df.drop()' function. 

8. ***In the year 2009-2010 show the percentage distribution of all the crops based on the area covered by each of the crops.***
    - `datafile_2.csv` has been considered in this question and the percentage distribution based on area for the crops has been considered.

9. ***What is the yield distribution of paddy in India?***
    - `datafile_1.csv` has been considered. The unwanted datas have been dropped and the required data i.e., *Crops,State,Yield* was considered and the remaining was dropped. Based on these datas a `Pie-Plot` has been plotted

10. ***Which state has the highest `cost of cultivation` for cotton ?***
    - `datafile_1.csv` has been considered and the column with `cost of cultivation` was selected and the rest was dropped and thereby with `df.idxmax()`, the index of the state having the maximum cost of cultivation was determined.

11. ***Which Kharif crop has the highest yield in the year 2011 ?***
    - `datafile_5.csv` was considered and the columns of *particulars* and *year was considered* and based on this the row was selected

12. Which crops are grown in Orissa and West Bengal both ?
    - `datafile_3.csv` was considered and the dataframes were created after cleaning the remaining unwanted data. Then filtering out the column of *State* for Orissa and West Bengal.

13. Prepare a comparative distribution of overall crop production for year 2009 denoting total yield
    - Based on `datafile_2.csv`, the *production* column for the year 2008-09 and 2009-10 was considered and two horizontal bar plots were constructed.

14. List the different varieties of paddy and wheat grown in India
    - `datafile_3.csv` was considered and the dataframe was formed based on both and the varieties column. The varieties were separately printed. 

15. Compare the production of rice, wheat, maize and bajra from 2006 to 2011
    - `datafile_3.csv` was taken under consideration and stacked bar chart was drawn based on these datas

---
> ## **References**

The websites that have been referred for this project are as follows :-
1. `www.geeksforgeeks.org`
2. `www.w3schools.com`
