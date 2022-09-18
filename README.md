# pds_final_projects
Repository for final project allocation and submission for CS60013 : Programming &; Data Structures offered in Autumn 2022 at IIT Kharagpur taught by Prof Subhamoy Mandal.

---
## Project Allocation
|Group Name  |     Student Groups                            | Project Allotted               |
|:----------:|:---------------------------------------------:|:-----------------------------:|
|Group 1     | KAVINPURI@KGPIAN.IITKGP.AC.IN, SOUMITAGURIAPHD22@KGPIAN.IITKGP.AC.IN | Project 1 |
|Group 2     | NAJAFARA.FATHIMA@KGPIAN.IITKGP.AC.IN, POOJA.JAIN@KGPIAN.IITKGP.AC.IN | [Project 4 : Medical Transcription Analysis](#project-4--medical-transcription-analysis) |
|Group 3     | MAMTA.RANI@KGPIAN.IITKGP.AC.IN, BHANUMEENA27@KGPIAN.IITKGP.AC.IN | Project 1 |
|Group 4     | DR.RAMKUMARKRISHNADHAS@KGPIAN.IITKGP.AC.IN, DRREFLEXPATEL94@KGPIAN.IITKGP.AC.IN | Project 1 |
|Group 5     | KAMLESHTONY10@KGPIAN.IITKGP.AC.IN, DRPRABHUKALYAN@KGPIAN.IITKGP.AC.IN | Project 1 |
|Group 6     | AMARMAJHI@KGPIAN.IITKGP.AC.IN, samriddha.das2000@kgpian.iitkgp.ac. | Project 1 |
|Group 7     | SAURABHCHAUDHARI97@KGPIAN.IITKGP.AC.IN, SATHISHBT@KGPIAN.IITKGP.AC.IN  | [Project 3 : ISBI 2022 Accepted Submissions Analysis](#project-3--isbi-2022-accepted-submissions-analysis) |

---
## Projects


### Project 1 : 





### Project 2 : Agriculture Crop Production Analysis
1. This project aims to analyse the crop production data from 2006 to 2011 from all the states of India. The dataset is located in the `data/crop_production/` directory. 
2. The data directory contains 5 csv files. Go through the data files and understand the data.
3. Different data files contain different types of data. For example `datafile_1.csv` contains the following fields:
    - `Crop` : Name of the crop
    - `State` : Name of the state
    - `Cost of Cultivation (/Hectare) A2+FL` : Cost of cultivation per hectare
    - `Cost of Cultivation (/Hectare) C2` : Cost of cultivation per hectare
    - `Cost of Production (/Quintal) C2` : Cost of production per quintal
    - `Yield (Quintal/ Hectare)` : Yield per hectare
4. The `datafile_2.csv` contains the following fields:
    - `Crop` : Name of the crop
    - `Production (YYYY - YY)` : Production of the crop between two consecutive years
    - `Area (YYYY - YY)` : Area of the crop between two consecutive years
    - `Yield (YYYY - YY)` : Yield of the crop between two consecutive years
    
5. Go through the data files and understand the data. You can use the `pandas` library to read the csv files and perform analysis on the data.
6. The data files are not clean. You need to clean the data before you start analysing it.
7. The project can be divided into the following parts:
    - `Data Processing`
        1. Writing the functions for reading the data files.
        2. Once you have read the data files, you need to clean the data. You can use the `pandas` library to clean the data.
        3. Only keep the data which is relevant to the analysis and drop the rest of the data.
    - `Data Analysis`
        1. In this part, you need to prepare a set of questions and answer them using the data provided.
        2. Answer `at least 15 questions` using the data provided.
        3. A few examples questions to get you started are as follows:
            - Which `crop` has the `highest production` in the country?
            - What are the major `states` where `rice` is grown?
            - What is the `average cost of cultivation` of `rice` in the country?
            - What are seasons where `Sunflower` is grown? (data availabe in `datafile_5.csv`)
            - What is average crop duration for `Paddy`, `Wheat` and `Maize`?
        4. You can come up with your own questions and answer them using the data provided.
    - `Data Visualization`
        1. Visualize the data using `matplotlib` or `seaborn` library.
        2. Visualizing the data will help you understand the data better and answer the questions.



### Project 3 : ISBI 2022 Accepted Submissions Analysis
1. The project aims to analyse the accepted submissions of ISBI 2022. The dataset is located in the `data/isbi2022/` directory. 
2. The dataset comprised of multiple `json` files. `JSON` stands for `J`avaScript `O`bject `N`otation. It is a lightweight data-interchange format. It is easy for humans to read and write. 
3. Each json file contain the information about multiple papers(about 100 papers in each). The information about the paper is stored in the form of key-value pairs. `JSON` is all about key-value pairs (aka `dictionaries` in Python).
4. Each paper contains more than 20 attributes, but the most useful attributes are listed as follows : 
   - `articleTitle` : Title of the paper
   - `authors` : List of authors of the paper
   - `citationCount` : Number of citations of the paper
   - `downloadCount` : Number of downloads of the paper
   -  `startPage` : Starting page of the paper
   -  `endPage` : Ending page of the paper
   -  `abstract` : Stripped abstract of the paper
5. The project can be divided into sub-areas as follows : 
   - `Data Preprocessing`
        1. Write functions to read to multiple json files and concatenate them into a single dataframe.
        2. Also only keep the useful attributes mentioned above and drop the rest.
   - `Data Analysis`
        1. In this part you can prepare a set of questions at least 15 and answer them using the dataset.
        2. Some examples questions to get you started:
            * On which `area` of ISBI 2022, the most number of papers were submitted?
            * Which are the `top 10` downloaded papers and what are they about?
            * Which are the `top 10` cited papers and what are they about?
            * What are the `mean` and `median` number of `authors` per paper?
            * Most common words in the abstracts of the papers? Form a `word cloud`.
            * What is the `average` number of `pages` per paper?
            * And so on... Get creative and come up with your own questions.
   - `Data Visualization`
        1. In this part you can make use of the `matplotlib` and `seaborn` libraries to visualize the answers to the questions you asked in the previous part.
        2. Everyone likes to see the results in the form of `graphs` and `charts`. So, make sure you visualize the answers to the questions you asked in the previous part.
   

### Project 4 : Medical Transcription Analysis
1. The project aims to analyse the medical transcription dataset. The dataset is located in the `data/medical_transcriptions/mtsamples.csv` directory.
2. The dataset is a `csv` file. `CSV` stands for `C`omma `S`eparated `V`alues. It is a simple file format used to store tabular data, such as a spreadsheet or database. Each line of the file is a data record. Each record consists of one or more fields, separated by commas. The use of the comma as a field separator is the source of the name for this file format.
3. The dataset contains following fields : 
   - `description` : Short brief of the interaction between the patient and the doctor.
   - `medical_specialty` : Medical specialty of the issue discussed in the transcription. 
   - `sample_name` : Medical Samples used for the diagnosis.
   - `transcription` : Full transcription of the interaction between the patient and the doctor.
   - `keywords` : Keywords of the transcription
4. The project can be divided into sub-areas as follows : 
   - `Data Preprocessing`
        1. Write functions to read the csv file. Suggestion : Use the `pandas` library.
        2. This dataset needs bit of pre-processing. The `medical_specialty` field contains multiple values. You need to split the values and create a list of values. For example, if the `medical_specialty` field contains `Orthopedics, Neurology`, then you need to split it into `['Orthopedics', 'Neurology']`.
        3. The keywords field contains multiple values. You need to split the values and transform it into a list of values. For example, if the `keywords` field contains `'pain, headache, migraine'`, then you need to split it into `['pain', 'headache', 'migraine']`.
        4. Look into the dataset and find out if there are any other fields that need to be pre-processed.
   - `Data Analysis`
        1. In this part you can prepare a set of questions at least 10 and answer them using the dataset.
        2. Some examples questions to get you started:
            * What is the `most common` medical specialty?
            * What is the `most common` medical sample?
            * What is the `most common` keyword?
            * What is the `average` length of the transcription?
            * What is the `average` length of the description?
            * What is the `average` length of the keywords?
            * And so on... Get creative and come up with your own questions.
   - `Data Visualization`
        1. In this part you can make use of the `matplotlib` and `seaborn` libraries to visualize the answers to the questions you asked in the previous part.
        2. Everyone likes to see the results in the form of `graphs` and `charts`. So, make sure you visualize the answers to the questions you asked in the previous part.



### Project 5




### Project 6




### Project 7


