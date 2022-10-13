# Final Projects for CS60013 : Programming and Data Structures
> Repository for final project allocation and submission for CS60013 : Programming &; Data Structures offered in Autumn 2022 at IIT Kharagpur taught by [Prof Subhamoy Mandal](https://sites.google.com/site/smandalbiomed/home).

> **Deadline** for project submission is **10th November 2022 at 23:59 IST**.

> This repository might be updated with new projects and/or changes to existing projects. Please check back regularly.

> Final projects are crafted by [Vinay](https://ummadiviany.github.io/) and [Sai Pavan](https://saipavan-tadem.github.io/) and approved by [Prof Subhamoy Mandal](https://sites.google.com/site/smandalbiomed/home).

- [Final Projects for CS60013 : Programming and Data Structures](#final-projects-for-cs60013--programming-and-data-structures)
  - [Instructions](#instructions)
    - [General Instructions](#general-instructions)
    - [Evaluation Policy](#evaluation-policy)
    - [Instructions to get started with the project](#instructions-to-get-started-with-the-project)
    - [What to submit](#what-to-submit)
    - [Submission Instructions](#submission-instructions)
    - [Deadline](#deadline)
  - [Project Allocation](#project-allocation)
  - [Projects](#projects)
    - [Project 1 : Medical Transcription Analysis](#project-1--medical-transcription-analysis)
    - [Project 2 : Agriculture Crop Production Analysis](#project-2--agriculture-crop-production-analysis)
    - [Project 3 : ISBI 2022 Accepted Submissions Analysis](#project-3--isbi-2022-accepted-submissions-analysis)
    - [Project 4 : Medical Image Visualization and Analysis](#project-4--medical-image-visualization-and-analysis)
    - [Project 5 : Patient Health Statistical Analysis](#project-5--patient-health-statistical-analysis)
  - [Resources](#resources)
  - [All the best!](#all-the-best)

---


## Instructions

### General Instructions
1. The project is to be done in groups of 3 students except (5th group). The students are expected to work together collaboratively.
2. The choice of programming language is left to the students. However, the most common languages used are Python and C/C++.
3. Each group will be assigned a mentor TA who will be responsible for guiding the group throughout the project.
4. Meetings with the mentor TA will be scheduled at the beginning of the project and at regular intervals.
5. Each student will be evaluated based on the contribution towards the project. Make sure you are contributing equally to the project.
6. Code plagiarism will not be tolerated. Any submission found to be plagiarized will be awarded a zero grade. 
7. Late submissions will not be accepted.
### Evaluation Policy
1. The final project evaluation is based on the following criteria:
   1. `Continuous Evaluation (CE) : 40%`
   2. `Code Quality and Documentation : 20%`
   3. `Final Submission and Report : 40%` 
2. `Continuous Evaluation (CE)` : 40%
   - The CE will be based on the following criteria:
      1. Your participation in the weekly meetings with your mentor TA.
      2. Your weekly progress and updates on the project.
3. `Code Quality and Documentation` : 20%
   - This will be based on the following criteria:
      1. Code Quality : 10% (based on the code quality and readability)
      2. Documentation : 10% (based on the documentation of the code and the project)
4. `Final Submission and Report` : 40%
   - This will be based on the following criteria:
      1. Final Submission : 20% (based on the final submission of the project)
      2. Final Report : 20% (based on the final report of the project)
5. CE will be evaluated if you have attended `at least 75%` of the weekly meetings with your mentor TA.


### Instructions to get started with the project
1. `Fork` this `github.com/ummadiviany/pds_final_projects` repository.
2. `Clone` the forked repository to your local machine using the following command:
   ```bash
   git clone github.com/{your_username}/pds_final_projects
   ```
3. Your projects are in the `submissions` directory. You can find the project description in the README.md file of the respective project directory.
4. Work on the project and make `regular commits` to your local repository and `push` them to your forked repository.
5. Your mentor TA will review your code and provide feedback.

### What to submit
1. You have to submit the following:
   1. `Final Code` : The final code of your project in the respective project directory. 
      1. Code should be highly readable and well documented.
      2. Try to write efficient code and avoid unnecessary code.
   2. `Final Report` : The final report of your project in the respective project directory. The report should be in the form of a `markdown` file with the name `report.md`. The report should contain the following:
      1. `Introduction` : A brief introduction of the project.
      2. `Data` : A brief description of the data used in the project.
      3. `Questions & Answers` : The questions and their respective answers. Also include the code snippets used to answer the questions and `who solved` the question.
      4. `References` : The references used in the project.

### Submission Instructions
1. Submission of the final project will be done via `GitHub Pull Requests`.
2. Once you are done with the project, you can create a `Pull Request` to the `main` branch of the `github.com/ummadiviany/pds_final_projects` repository.
3. We will review your merge request and provide feedback. You can make changes to your code and update the merge request. If accepted, your project will be merged to the `main` branch of the `github.com/ummadiviany/pds_final_projects` repository.
4. That's it! `Congratulations!!` have successfully submitted your final project.

### Deadline
The deadline for the final project submission is **10th November 2022, 23:59 IST**.

## Project Allocation
|     Students                            | Project                |  Mentor TA    |
|:---------------------------:|:-----------------------------:|:------------------:|
| Amar Majhi, Mamta Rani, Reflex Kumar Patel| [Project 4 : Medical Image Visualization and Analysis](#project-4--medical-image-visualization-and-analysis) | Sai Pavan |
| Bhanu Kumar Meena, Syeda Najafara Fathima, Kavin Puri | [Project 1 : Medical Transcription Analysis](#project-1--medical-transcription-analysis) | Vinay |
| Pooja P Jain, Sathishkumar S, P.V.Kamlesh | [Project 3 : ISBI 2022 Accepted Submissions Analysis](#project-3--isbi-2022-accepted-submissions-analysis) | Vinay |
| Ramkumar K, Chaudhari Saurabh Santosh, Samriddha Das | [Project 2 : Agriculture Crop Production Analysis](#project-2--agriculture-crop-production-analysis) | Vinay |
| Prabhukalyan Dash, Soumita Guria | [Project 5 : Patient Health Statistical Analysis](#project-5--patient-health-statistical-analysis) | Sai Pavan |

---
## Projects

### Project 1 : Medical Transcription Analysis
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
   

### Project 4 : Medical Image Visualization and Analysis
1. The project aims to read, visualize and analyze the medical images. The dataset is located in the `data/medical_images/` directory.
2. The dataset contains medical images of `MRI` and `CT` scans for different anatomical parts of the body. It also contains the `segmentation masks` for the images.
3. The dataset has
   1. `Hippocampus MRI` images and segmentation masks
   2. `Heart MRI` images and segmentation masks
   3. `Prostate MRI` images and segmentation masks
   4. `Abdomen CT` images and segmentation masks
4. These scans are used to diagnose the diseases of the body. The segmentation masks are used to identify the different parts of the body in the images.
5. Scans are in `NIFTI` format. `NIFTI` is a standard format for storing medical images.
6. All the scans are `3D Volumes`. Each 3D volume is a stack of `2D images`. Each 2D image is called a `slice`.
7. Your first task is to read the images and visualize them. You can use the `nibabel` library to read the images.
8. Visualizing the images is important to understand the data. You can use the `matplotlib` library to visualize the images. Visualization can be done in multiple ways. You can visualize the images in the following ways:
   1. Visualize the `slices` of the images and the segmentation masks.
   2. Visualize the `3D volumes` of the images and the segmentation masks.
9. The next task is to analyze the images. You can use the `numpy` library to analyze the images. The analysis part is open ended. 
10. You can perform simple statistical analysis on the images. You can also perform more complex analysis like `image segmentation` and `image classification`.
11. Statistical analysis may include the following:
    1. Calculate the `mean`, `median`, `standard deviation`, `minimum` and `maxmum` for the whole image, segmented image.
    2. Now compare the statistics of the segmented image with the whole image. What do you observe?
12. Complex analysis may include the following:
    1. Perform `image segmentation` on the images. You can use the `scikit-image` library to perform image segmentation.
    2. Perform `image classification` on the images. You can use the `scikit-learn` library to perform image classification.
    3. You can also perform `image registration` on the images. You can use the `SimpleITK` library to perform image registration. 
12. Try with statistical analysis first and then move on to more complex analysis. Although, we do not expect you to perform complex analysis, you can try it if you want to.
13. Remember, the analysis part is open ended. You can come up with your own analysis ideas and implement them.

### Project 5 : Patient Health Statistical Analysis

1. Create a .csv file which contain the following information

      - create an attribute with name `patient` Ten names of your friends or Random names-`string` format
      - add the attribute `patient Identifier` and assign 1 to 10 digits for each person-integer format.
      - add the attribute `Height` and add the respective heights in `float` format

            {5.5,5.6,6.1,6.1,6.0,5.9,5.8,5.8,5.8,9.1}  Float format

      - add the attribute `Temperature` and add the respective heights in `float` format

            {97.2,97.3,97.8,98,98.1,98.2,97.3,98,101,102}  Float format

      - add the attribute '`disease` and assign the following as per their patient identifier

            Randomly assign the disease to patients with the following
              {Headeach ,cold ,fever}

      - add the attribute `Hospital` and assign the following as per the patient identifier randomly.

      - add the attribute `Cost` and assign the following as per the patient identifier randomly.

            {20.0,1000.0,800.0,910.0,950.0,980.0,990.0,890.0,880.0,930.0}  Float format

2. Obtain the statistics from the dataset you created
      - Now create the class to represent the same above data
      - create the methods to calculate the statistics
            
            Mean ,Median ,Mode of 'Height'
            Mean ,Median ,Mode of 'Cost'
            Mean ,Median ,Mode of 'Temperature'
3. comment on the statistic calculations and clearly mention your observation 
          
         Note: This section may hold high weightage so write the observations in short and specific to point.

---
## Resources
1. [Python Documentation](https://docs.python.org/3/)
2. [Class Code Materials](https://github.com/ummadiviany/pds_snippets/)
3. [Introduction to Computation and Programming Using Python](https://mitpress.mit.edu/9780262542364/introduction-to-computation-and-programming-using-python/)
4. [Elements of Programming Interviews in Python]()
5. Python Libraries
   1. [Matplotlib : For awesome visualizations](https://matplotlib.org/)
   2. [Pandas : For data analysis](https://pandas.pydata.org/)
   3. [Numpy : For numerical computations](https://numpy.org/)

---
## All the best!
