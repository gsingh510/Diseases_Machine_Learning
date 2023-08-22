# Diseases Machine Learning
## Overview
In this project,  we develop a ML machine that can ingest new sample set data and refine the predictions based on user inputted parameters. The output from the data collected would predict the likelihood that the user has a disease or not and reccomend they follow up with their medical provider. 

## Analysis by
- [Alex Storton](https://github.com/astorton)
- [Bruce Skaar](https://github.com/bskaar)
- [Gagandeep Singh](https://github.com/gsingh510)
- [Mwohania Taylor](https://github.com/nia12taylor)
- [Niti Patel](https://github.com/niti2442)
- [Skyler Khalachyan](https://github.com/SkylerKhalachyan)

# Project Outline

## Introduction
The instructions for this project were separated into four subsections: Data Model Implementation, Data Model Optimization, GitHub Documentation, Group Presentation. 

## Instructions

1. Create the user interface.
2. Write client-side Python.
3. Connect the app to the notebook.
4. Deploy the app.

## Installation

1. Clone the repository.
2. Open the [Project4Group3Final](https://github.com/gsingh510/Diseases_Machine_Learning/tree/44f7832aef4e4b69a4c114b67fd2cd8a16fd4271/Project4Group3Final) folder in VS code. 
3. Please install the required Python packages via the "requirements.txt" file before running the Webapp.py
   [Requirements File Link](https://github.com/gsingh510/Diseases_Machine_Learning/blob/44f7832aef4e4b69a4c114b67fd2cd8a16fd4271/Project4Group3Final/requirements.txt)
4. Once the Flask App server is online, take your Dash http enviorment and open in a new tab (preferably Google Chrome).
5. Once opened you will be able to interact with the Dashboard and run the Machine Learning Model. 

## Features

- Use Python to initialize, train, and evaluate the model
- Clean data in preparation of modeling
- Display up to 75% accuracy for the model

## Data Sources and Data Models

Within resources folder:

[Disease Dataset](https://github.com/gsingh510/Diseases_Machine_Learning/tree/70cadf738cf96822ea967d40323ba2d4b62cde52/Project4Group3Final/Data)

[Data Models](https://github.com/gsingh510/Diseases_Machine_Learning/tree/70cadf738cf96822ea967d40323ba2d4b62cde52/Models)


## Overview of our data
![alt text](https://github.com/gsingh510/Diseases_Machine_Learning/blob/d5bd1825ee3608a1423cece974a8e59f6ca8b21e/Data%20Images/Screen%20Shot%202023-08-21%20at%2010.27.17%20AM.png)

## Top Diseaes amoung Females and Males from our data source 
![alt text](https://github.com/gsingh510/Diseases_Machine_Learning/blob/d5bd1825ee3608a1423cece974a8e59f6ca8b21e/Data%20Images/Screen%20Shot%202023-08-21%20at%2010.27.29%20AM.png)

## Built With

- Python
- Jupyter Notebook
- Tableau
- Google Collab

## Project Outline

Introduction:

-Predict patient disease based on their symptoms, blood pressure and cholesterol readings and demographics (age, gender)
-Our proposed solution: Develop a web app that runs a ML model that ingests user input parameters and produces an output that predicts whether or not a person is likely to have a disease based on their current symptoms and demographics. If the results are positive, our model would suggest that a disease is likely and that they should follow up with their provider. 

Data Model_Implementation:
-- Four models selected; Logistic Regression (LR), Neural Network (NN), Random Forest (RF) and Decision Tree (DT)
--Supervised learning models only
--All use same data pre-processing code
--Same target variable
--Label encode all categorical data
--“Age” was the only feature scaled for the modeling

-Data Model_Optimization

Logisitic Regression - 57.6%:

Iteration 1- 2.3%
-Features are one hot encoded
-Disease is set as the target variable

Iteration 2- 51%
-The target variable is updated to the outcome variable
-Features are label encoded
-Disease is removed from the features

Iteration 3- 57.6%
-The age and fatigue features are removed

Neural Network - 65.9%:

Iteration 1- 2.1%
-Features are one hot encoded
-Disease is set as the target variable

Iteration #2 (56.8%)
-Epoch Count decreased
-Only 2 hidden layers

Iteration #3 (64.7%)
-Set ReLU as activation parameter for all layers
-Removed “Fatigue” Feature
-Hidden layer count set to 4
-Reduced neural nodes by half (decrementing by 50% for each)

Iteration #3 (Final)
Added learning rate parameter to compiler
Increase epoch count by 10

Random Forest - 79.5%
-Only one iteration implemented
-Beneficial for 
data that appears to be overfitting
-Works well with non-linear data
-Used to help provide insights on the features themselves

Decision Tree:


Challenge & Barriers:
-Label encoding vs One Hot Encoder 
-Deciding which columns to drop
-Linking up our app to our dashboard and getting it to run our prediction model 
-Neural network model proved to be too complex for the relatively small data set

Future Opportunities:

-Having a significantly larger dataset. 
-Solve TensorFlow issues in running our Webapp. 
-Push the model(s) to 90% accuracy threshold
-Integrate Tableau visualizations into the web app
-Integrate a web scraper to pull local doctors that specialize in the diseases based on user entered zip code and display summary info (contact, ratings, etc) 



## Acknowledgements
Program: University of California Berkeley Data Analytics Bootcamp

Instructor: Ahmad Sweed

TA’s: Venkata Kuppa, Karen Fisher, Brian Perry, Ryan Bernstein
   

   
