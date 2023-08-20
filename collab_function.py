# Import the modules
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.metrics import balanced_accuracy_score, confusion_matrix, classification_report, accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
from imblearn.over_sampling import RandomOverSampler
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from keras.metrics import categorical_accuracy
import tensorflow as tf
import glob
import os
from joblib import dump


def load_data():
    # load 
    disease_training = pd.read_csvI("Data/Disease_symptom_and_patient_profile_dataset.csv", encoding="utf-8") #load data into a data frame
    
    # clean / label
    labeled_df = label_data(disease_training)
    
    return labeled_df

def label_data(disease_df):
    #Create an instance of LabelEncoder
    label_encoder = LabelEncoder()

    #Label encode everything except age

    #disease_df.apply(label_encoder.fit_transform)

    #disease_df['Disease','Outcome Variable','Gender','Difficulty Breathing','Fever','Cough','Fatigue','Blood Pressure','Cholesterol Level'] = label_encoder.fit_transform(disease_df['Disease','Outcome Variable','Gender','Difficulty Breathing','Fever','Cough','Fatigue','Blood Pressure','Cholesterol Level'])

    #Encoding Disease Column
    #disease_df['Disease'] = label_encoder.fit_transform(disease_df['Disease'])
    disease_df['Outcome Variable'] = label_encoder.fit_transform(disease_df['Outcome Variable'])
    disease_df['Gender'] = label_encoder.fit_transform(disease_df['Gender'])
    disease_df['Difficulty Breathing'] = label_encoder.fit_transform(disease_df['Difficulty Breathing'])
    disease_df['Fever'] = label_encoder.fit_transform(disease_df['Fever'])
    disease_df['Cough'] = label_encoder.fit_transform(disease_df['Cough'])
    disease_df['Fatigue'] = label_encoder.fit_transform(disease_df['Fatigue'])
    disease_df['Blood Pressure'] = label_encoder.fit_transform(disease_df['Blood Pressure'])
    disease_df['Cholesterol Level'] = label_encoder.fit_transform(disease_df['Cholesterol Level'])

    # disease_df.drop(["Fever", "Cough", "Fatigue", "Difficulty Breathing", "Gender", "Blood Pressure", "Cholesterol Level", "Outcome Variable"], axis=1, inplace=True)
    disease_df

def train_model():
    ## call load_date -> which is then going to call  label data 
    disease_df = load_data()
    
    # split the data 
    
    X = disease_df.copy()
    X.drop(["Outcome Variable","Disease"], axis=1, inplace=True)
    X.head()
    
    y = disease_df["Outcome Variable"].values.reshape(-1,1)
    y[:5]
    
    X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=12)
    
    scaler = StandardScaler()
    scaler.fit(X_train)
    
    X_train_scaled = scaler.transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    model = tree.DecisionTreeClassifier()
    
    model = model.fit(X_train_scaled, y_train)
    
    predictions = model.predict(X_test_scaled)
    
    ## fill in rest of the code ^^ copy to the point of model is ready to execuute 
    
    return model 

def recommendation(fever, cough, fatigue, cl, cb):
    # create a model 
    model = train_model() 
    
    pred = model.predict(fever, cough, fatigue, cl, cb)
    return pred