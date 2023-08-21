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
from joblib import dump

predictions = None
scaler = StandardScaler()

def load_data():
    # load 
    disease_training = pd.read_csv("./Data/Disease_symptom_and_patient_profile_dataset.csv", encoding="utf-8") #load data into a data frame
    
    # clean / label
    labeled_df = label_data(disease_training)
    
    return labeled_df

def label_data(disease_df):
    #Create an instance of LabelEncoder
    label_encoder = LabelEncoder()

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

    return disease_df

def train_model():
    ## call load_date, which is then going to call label data 
    disease_df = load_data()
    
    # split the data 
    
    X = disease_df.copy()
    X.drop(["Outcome Variable","Disease"], axis=1, inplace=True)
    X.head()
    
    y = disease_df["Outcome Variable"].values.reshape(-1,1)
    y[:5]

    global predictions
    
    X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=12)

    scaler.fit(X_train)

    X_train_scaled = scaler.transform(X_train)
    X_test_scaled = scaler.transform(X_test)
        
    model = tree.DecisionTreeClassifier()
    
    model = model.fit(X_train_scaled, y_train)

    predictions = model.predict(X_test_scaled)

    acc_score = accuracy_score(y_test, predictions)
        
    return model, acc_score

def recommendation(fever, cough, fatigue, breathing, age, gender, bp, cl):
    # createing a model 
    model, acc_score = train_model() 

    test_data = {
        "Fever": fever,
        "Cough": cough,
        "Fatigue" : fatigue,
        "Difficulty Breathing": breathing,
        "Age": age,
        "Gender": gender,
        "Blood Pressure": bp,
        "Cholesterol Level": cl
    }

    # data transformation 
    test_df = pd.DataFrame(test_data, index=[0])
    test_df_scaled = scaler.transform(test_df) 

    # predict using the model
    pred = model.predict(test_df_scaled)

    return pred[0], acc_score # returning the prediction and accuracy scores from the model given the user inputs 