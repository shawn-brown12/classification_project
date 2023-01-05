# Churn within the Realm of Telecom

# Project Description

The main goal of this project is to take in the Telco_churn dataset, which is about customers of a telecommunications company. Using that data to find out what makes customers leave I will create multiple Classification models to better predict when a customer will churn, and then make recommendations based on my findings to keep customers.

# Project Goals

- Discovers the biggest drivers of customer churn.

- Use those drivers to develpo machine learning models to accurately classify customers as either churned or not churned.

- Deliver a report that a non-techincal person can read and understand what steps were taken, why they were taken, and the outcomes from those steps.

# Initial Hypothesis and Questions

My initial hypothesis is that the biggest drivers of churn will be their contract type, whether or not they have internet and phone services, and what type of internet they have.

My main questions to determine this:

- Is whether or not a customer churns independent of their internet service type?

- Are contract type and churn status related?

- What is the relationship between phone service and churn?

- Does gender factor into churn?

- Do monthly charges differ for different contract types?

# Data Dictionary 

| **Feature | Definition** |
|:--------|:-----------|
|senior_citizen| 1 or 0, 1 being they *are* a senior citizen and 0 being the opposite|
|tenure| The number of months a customer has been with the company|
|monthly_charges| How much that customer's monthly bill is|
|total_charges| The total amount that the customer has paid the company|
|churn| True or False, True being the customer *has* churned, and False being otherwise|
|gender_Male| 1 o 0, 1 being that the customer is a male, a 0 being that they're female|
|partner_Yes| 1 or 0, 1 being that the customer has a partner, 0 if otherwise|
|dependents_Yes| 1 or 0, 1 being that the customer has dependents, and 0 if otherwise|
|phone_service_Yes| 1 or 0, 1 being that the customer has phone service with the company, and 0 if otherwise|
|multiple_lines_Yes| 1 or 0, 1 being that the customer has multiple lines and 0 if otherwise|
|online_security_Yes| 1 or 0, 1 being that the customer has online security, and 0 if otherwise|
|online_backup_Yes| 1 or 0, 1 being that the customer has online back, and 0 if otherwise|
|device_protection_Yes| 1 or 0, 1 being that the customner has online backup and 0 if otherwise|
|tech_support_Yes| 1 or 0, 1 being that the customer has tech support, and 0 if otherwise|
|streaming_tv_Yes| 1 or 0, 1 being that the customer has tech support, and 0 if otherwise
|streaming_movies_Yes| 1 or 0, 1 being that the customer has tech support, and 0 if otherwise|
|paperless_billing_Yes| 1 or 0, 1 being that the customer has paperless billing, and 0 if otherwise|
|contract_type_Month-to-month| 1 or 0, 1 being that the customers contract type is month-to-month, and 0 if otherwise|
|contract_type_One year| 1 or 0, 1 being that the customers contract type is 1 year long, and 0 if otherwise|
|contract_type_Two year| 1 or 0, 1 being that the customers contract is 2 years long, and 0 if otherwise|
|internet_service_type_DSL| 1 or 0, 1 being that the customers internet type is DSL, and 0 if otherwise|
|internet_service_type_Fiber optic| 1 or 0, 1 being that the customers internet type is fiber optic, and 0 if otherwise|
|internet_type_None| 1 or 0, 1 being that the customer doesn't have internet, and 0 being that they do|
|payment_type_Bank transfer (automatic)| 1 or 0, 1 being that the customers payment type is an automatic bank payment, and 0 if otherwise|
|payment_type_Credit card (automatic)| 1 or 0, 1 being that a customers payment type is automatic through a credit card, and 0 if otherwise|
|payment_type_Electronic check| 1 or 0, 1 being that the customers payment type is an electronic check, and 0 if otherwise|
|payment_type_Mailed check| 1 or 0, 1 being if the customers payment type is a mailed check, and 0 if otherwise|

# My Plan

- Acquire and Prepare my data via my acquire.py and prepare.py files and the functions within.

- Verify that my functions performed correctly, and my data is prepared how I need it.

- Explore my data further to determine drivers of churn.

- Answer my initial questions.

- Develop a model to determine if a customer will churn by:

        - Using the drivers identified from my initial questions. 
        
        - Evaluate my models based on my train and validate datasets.
        
        - Select my top three performing models based upon accuracy.
        
        - Of those three, evaluate the best model with my test data.
        
- Draw conclusions.

# Steps to Reproduce

- Clone this repo.

- Acquire this data, either through Codeup or elsewhere.

- Put the data in the file with the cloned repo.

- Run the notebook.

# Takeaways and Conclusions

- Roughly 1/4 of customers churn.

- The biggest driver of churn seems to be the customers contract type; When a customer has a month-to-month contract, churn is just over 40%, or 2/5.

- Internet service type also plays a significant role in churn, though not as large as their contract type.

- Customers with fiber optic internet churned much more than those with either no internet or DSL.

- Whether or not a customer has phone service doesn't play a significant role in churn.

- Neither age or gender have much of an effect on whether or not someone will churn.

- Monthly charges also seem to play a role in churn.

- The final model beats the baseline accuracy for predicting whether someone will churn by about 8%.

# Recommendations

- Provide better support for customers with fiber optic internet.

- Make improvements to month to month contract plans to make it more appealing to customers.

- Alternatively, or in addition to the above, make the one and two year contract types more appealing as customers with those churned significantly less.

- Failing making any significant changes to the month-to-month contracts, maybe sending out emails to those customers most likely to churn, offering a deal or even just sending out surveys would be potentially helpful.