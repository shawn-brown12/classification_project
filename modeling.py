import os
import pandas as pd
import numpy as np
import seaborn as sns
from scipy import stats
from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, plot_confusion_matrix

def split_train_test(df, col):
    
    seed = 42
    train, val_test = train_test_split(df, train_size=.5, random_state=seed, stratify=df[col])
    validate, test = train_test_split(val_test, train_size=.6, random_state=seed, stratify=val_test[col])
    
    return train, validate, test

def make_baseline(df, baseline, col):
    '''
    This function is used to create a column within the dataframe to make a baseline column, and then calculate the baseline accuracy. Needs to be optimized more, but functions as is currently. Make sure to use the word 'baseline' when calling function.
    '''
    
    seed = 42
    
    df[baseline] = df[col].value_counts().idxmax()    

    base = (df[col] == df[baseline]).mean()
    
    print(f'Baseline Accuracy is: {base:.3}')
    
def xy_train(train, validate, test):
    '''
    This function will separate each of my datasets (train, validate, and test) and split them further into my x and y sets for modeling. When running this, be sure to assign each of the six variables in the proper order, otherwise it will almost certainly mess up. (X_train, y_train, X_validate, y_validate, X_test, y_test).
    '''
    
    seed = 42
    
    X_train = train.drop(columns=['contract_type', 
                                  'internet_service_type', 
                                  'churn_Yes',
                                  'customer_id'])
    y_train = train.churn_Yes

    X_validate = validate.drop(columns=['contract_type', 
                                   'internet_service_type', 
                                   'churn_Yes',
                                   'customer_id'])
    y_validate = validate.churn_Yes

    X_test = test.drop(columns=['contract_type', 
                                'internet_service_type', 
                                'churn_Yes',
                                'customer_id'])
    y_test = test.churn_Yes
    
    return X_train, y_train, X_validate, y_validate, X_test, y_test

def rf_gen(df, col):
    
    metrics = []

    for i in range(1, 20):
    
        '''
        This function will create a dataframe of Random Forest models of varying max_depths and compare the differences from the train and validate sets and return the dataframe. It requires the variable names to be: X_train, y_train, X_validate, and y_validate.
        '''
        
        train, validate, test = split_train_test(df, col)
        X_train, y_train, X_validate, y_validate, X_test, y_test = xy_train(train, validate, test)
        
        rf = RandomForestClassifier(max_depth=i, min_samples_leaf=3, n_estimators=200, random_state=42)
        rf = rf.fit(X_train, y_train)
        
        in_sample_accuracy = rf.score(X_train, y_train)
        out_of_sample_accuracy = rf.score(X_validate, y_validate)
        output = {
            "max_depth": i,
            "train_accuracy": in_sample_accuracy,
            "validate_accuracy": out_of_sample_accuracy
            }
    
        metrics.append(output)
    
    df = pd.DataFrame(metrics)
    df["difference"] = df.train_accuracy - df.validate_accuracy
    return df

def dectree_gen(df, col):
    
    metrics = []

    for i in range(1, 20):
    
        '''
        This function will create a dataframe of Decision Tree models of varying max_depths and compare the differences from the train and validate sets and return the dataframe. It requires the variable names to be: X_train, y_train, X_validate, and y_validate.
        '''
        train, validate, test = split_train_test(df, col)   
        X_train, y_train, X_validate, y_validate, X_test, y_test = xy_train(train, validate, test)
        
        dectree = DecisionTreeClassifier(max_depth=i, random_state=42)
        dectree = dectree.fit(X_train, y_train)

        in_sample_accuracy = dectree.score(X_train, y_train)
        out_of_sample_accuracy = dectree.score(X_validate, y_validate)
        output = {
            "max_depth": i,
            "train_accuracy": in_sample_accuracy,
            "validate_accuracy": out_of_sample_accuracy
            }
    
        metrics.append(output)
    
    df = pd.DataFrame(metrics)
    df["difference"] = df.train_accuracy - df.validate_accuracy
    return df


def knn_gen(df, col):
    
    metrics = []

    for i in range(1, 21):
    
        '''
        This function will create a dataframe of KNN models of varying n_neighbors and compare the differences from the train and validate sets and return the dataframe. It requires the variable names to be: X_train, y_train, X_validate, and y_validate.
        '''
        
        train, validate, test = split_train_test(df, col)   
        X_train, y_train, X_validate, y_validate, X_test, y_test = xy_train(train, validate, test)
        
        knn = KNeighborsClassifier(n_neighbors=i, weights='uniform')
        knn = knn.fit(X_train, y_train)

        in_sample_accuracy = knn.score(X_train, y_train)
        out_of_sample_accuracy = knn.score(X_validate, y_validate)
        output = {
            "max_depth": i,
            "train_accuracy": in_sample_accuracy,
            "validate_accuracy": out_of_sample_accuracy
            }
    
        metrics.append(output)
    
    df = pd.DataFrame(metrics)
    df["difference"] = df.train_accuracy - df.validate_accuracy
    return df