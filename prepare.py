import os
import pandas as pd
from env import host, username, password
from sklearn.model_selection import train_test_split

#function to turn a dataset into train, validate, and test subsets
def split_train_test(df, col):
    
    seed = 69
    train, val_test = train_test_split(df, train_size=.5, random_state=seed, stratify=df[col])
    validate, test = train_test_split(val_test, train_size=.6, random_state=seed, stratify=val_test[col])
    
    return train, validate, test

#function to prepare telco_churn dataset for use
def prep_telco(df):
    to_drop = ['Unnamed: 0', 'payment_type_id', 'internet_service_type_id', 'contract_type_id', 'customer_id', ]
    df.drop(columns=to_drop, inplace=True)
    
    to_dummy = ['gender', 'partner', 'dependents', 'phone_service', 'multiple_lines', 'online_security', 
                'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies', 
                'paperless_billing', 'churn', 'contract_type', 'internet_service_type', 
                'payment_type']
    
    dummies = pd.get_dummies(to_dummy, drop_first=True)
    df = pd.concat([df, dummies], axis=1)
    return df