# Churn within the Realm of Telecom

# Project Description

The main goal of this project is to take in data about customers of a telecommunications company, and,  using that, find out what makes customers leave, and make recommendations based on my findings. 

# Project Goals

- Discovers the biggest drivers of customer churn.

- Use those drivers to develpo machine learning models to accurately classify customers as either churned or not churned.

- Deliver a report that a non-techincal person can read and understand what steps were taken, why they were taken, and the outcomes from those steps.

# Initial Hypotheses and Questions

My initial hypothesis is that the biggest drivers of churn will be their contract type, whether or not they have internet and phone services, and what type of internet they have.

My main questions to support this:

- Does internet service type and churn have a relationship?

- Does contract type affect churn status?

- Are phone service and internet service related?

- Does gender or age factor into churn?

- Do monthly charges different for different contract types?

# Data Dictionary 

| Feature | Definition |
|:--------|:-----------|
|senior_citizen| 1 or 0, 1 being they *are* a senior citizen and 0 being the opposite|
|tenure| The number of months a customer has been with the company|
|monthly_charges| How much that customer's monthly bill is|
|total_charges| The total amount that the customer has paid the company|
|churn| True or False, True being the customer *has* churned, and False being otherwise|
|gender_Male| 1 o 0, 1 being that the customer is a male, a 0 being that they're female|
|partner_Yes| 1 or 0, 1 being that the customer has a partner, 0 being otherwise|
|dependents_Yes| 1 or 0, 1 being that the customer has dependents, and 0 being otherwise|
|phone_service_Yes| 1 or 0, 1 being that the customer has phone service with the company, and 0 being otherwise|
|multiple_lines_Yes| 1 or 0, 1 being that the customer has multiple lines and 0 being otherwise|
|online_security_Yes| 1 or 0, 1 being that the customer has online security, and 0 being otherwise|
|online_backup_Yes| 1 or 0, 1 being that the customer has online back, and 0 being otherwise|
|device_protection_Yes| 1 or 0, 1 being that the customner has online backup and 0 being otherwise|
|tech_support_Yes| 1 or 0, 1 being that the customer has tech support, and 0 being otherwise|
|streaming_tv_Yes| 1 or 0, 1 being that the customer has tech support, and 0 being otherwise
|streaming_movies_Yes| 1 or 0, 1 being that the customer has tech support, and 0 being otherwise|
|paperless_billing_Yes| 1 or 0, 1 being that the customer has paperless billing, and 0 being otherwise|
|contract_type_Month-to-month| 1 or 0, 1 being that the customers contract type is month-to-month, and 0 being otherwise|
|contract_type_One year| 1 or 0, 1 being that the customers contract type is 1 year long, and 0 otherwise|
|contract_type_Two year| 1 or 0, 1 being that the customers contract is 2 years long, and 0 otherwise|
|internet_service_type_DSL| 1 or 0, 1 being that the customers internet type is DSL, 0 otherwise|
|internet_service_type_Fiber optic| 1 or 0, 1 being that the customers internet type is fiber optic, and 0 otherwise|
|internet_type_None| 1 or 0, 1 being that the customer doesn't have internet, and 0 being that they do|
|payment_type_Bank transfer (automatic)| 1 or 0, 1 being that the customers payment type is an automatic bank payment, and 0 otherwise|
|payment_type_Credit card (automatic)| 1 or 0, 1 being that a customers payment type is automatic through a credit card, and 0 if otherwise|
|payment_type_Electronic check| 1 or 0, 1 being that the customers payment type is an electronic check, and 0 otherwise|
|payment_type_Mailed check| 1 or 0, 1 being if the customers payment type is a mailed check, 0 otherwise|

# My Plan

- Acquire and Prepare my data via my acquire.py and prepare.py files and the functions within

- Verify that my functions performed correctly, and my data is prepared how I need it

- Answer my initial questions

- Develop a model to determine if a customer will churn by:

        - using the drivers identified from my initial questions 
        
        - Evaluate my models based on my train and validate datasets
        
        - Select my top three performing models based upon accuracy
        
        - Of those three, evaluate the best model with my test data
        
- Draw conclusions

# Takeaways and Conclusions

# Recommendations
>>>>>>> f602b3b (uploading updated readme and acquire and prepare files)
