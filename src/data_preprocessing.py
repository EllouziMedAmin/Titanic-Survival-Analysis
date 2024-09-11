
import pandas as pd

def clean_data(df):
    # Drop columns with too many missing values
    df = df.drop(columns=['cabin', 'boat', 'body', 'home.dest'])
    
    # Fill missing age with median age
    df['age'].fillna(df['age'].median(), inplace=True)
    df['fare'].fillna(df['fare'].median(), inplace=True)   
    # Fill missing embarked with mode
    df['embarked'].fillna(df['embarked'].mode()[0], inplace=True)
    
    # Convert categorical variables to numerical
    df['sex'] = df['sex'].map({'male': 0, 'female': 1})
    df['embarked'] = df['embarked'].map({'C': 0, 'Q': 1, 'S': 2})
    
    return df

