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
    '''
    This function will prepare the telco_churn dataset for further use. It will convert the total_charges column into the float 
    data type, create various dummies and concatenate those dummies, and then drop unneeded columns.
    '''
    df['total_charges'] = df['total_charges'].replace(' ', '0')
    df['total_charges'] = df['total_charges'].astype(float)
    df['churn'] = df['churn'].astype(bool)
    
    to_dummy = ['gender', 'partner', 'dependents', 'phone_service', 'multiple_lines', 'online_security', 
                'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies', 
                'paperless_billing', 'contract_type', 'internet_service_type', 
                'payment_type']
    dummies = pd.get_dummies(df[to_dummy], drop_first=False)
    df = pd.concat([df, dummies], axis=1)
    
    drop = ['multiple_lines_No phone service', 'online_security_No internet service',
        'online_backup_No internet service', 'device_protection_No internet service',
        'tech_support_No internet service', 'streaming_tv_No internet service',
        'streaming_movies_No internet service', 'gender_Female', 'partner_No',
        'dependents_No', 'phone_service_No', 'multiple_lines_No',           'online_security_No', 'online_backup_No',
        'device_protection_No', 'tech_support_No', 'streaming_tv_No',
        'streaming_movies_No', 'paperless_billing_No', 'gender', 'partner', 
        'dependents', 'phone_service', 'multiple_lines', 'online_security', 
        'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies', 
        'paperless_billing', 'contract_type', 'internet_service_type', 
        'payment_type', 'Unnamed: 0', 'payment_type_id', 'internet_service_type_id', 
        'contract_type_id', 'customer_id']
    df.drop(columns=drop, inplace=True)
                 
    return df