import os
import pandas as pd
from env import host, username, password
#this will connect to Codeup mysql server if this function is within the env.py file in directory


def get_connection(db, user=username, host=host, password=password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def get_telco_data():
    '''
    This function will check locally if there's a telco.csv file in the local directory, and if not, working with the 
    get_connection function, will pull the telco dataset from the Codeup MySQL server. After that, it will also save a copy of 
    the csv locally if there wasn't one, so it doesn't have to run the query each time.
    '''
    if os.path.isfile('telco.csv'):
        return pd.read_csv('telco.csv')
    else:
        url = get_connection('telco_churn')
        query = '''
                SELECT *
                FROM customers
                JOIN contract_types USING(contract_type_id)
                JOIN internet_service_types USING (internet_service_type_id)
                JOIN payment_types types USING(payment_type_id);
                '''
        telco = pd.read_sql(query, url)
        telco.to_csv('telco.csv')
        return 