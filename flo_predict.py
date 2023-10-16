###############################################################
# Customer Segmentation with RFM
###############################################################

###############################################################
# Business Problem
###############################################################
# FLO wants to segment its customers and determine marketing strategies based on these segments.
# Customer behaviors will be defined, and groups will be created based on these behavioral clusters.

###############################################################
# Dataset Story
###############################################################

# The dataset consists of information derived from the past shopping behaviors of customers who made their last purchases in 2020-2021 through OmniChannel (both online and offline shopping).

# master_id: Unique customer number
# order_channel: Which channel was used for the purchase (Android, iOS, Desktop, Mobile, Offline)
# last_order_channel: The channel where the last purchase was made
# first_order_date: The date of the customer's first purchase
# last_order_date: The date of the customer's last purchase
# last_order_date_online: The date of the customer's last online purchase
# last_order_date_offline: The date of the customer's last offline purchase
# order_num_total_ever_online: Total number of purchases made by the customer online
# order_num_total_ever_offline: Total number of purchases made by the customer offline
# customer_value_total_ever_offline: Total amount paid by the customer in offline purchases
# customer_value_total_ever_online: Total amount paid by the customer in online purchases
# interested_in_categories_12: List of categories the customer shopped in the last 12 months

###############################################################
# TASKS
###############################################################

# TASK 1: Data Understanding and Preparation
import pandas as pd

# 1. Read the flo_data_20K.csv dataset.
# 2. In the dataset,
# a. First 10 observations,
# b. Variable names,
# c. Descriptive statistics,
# d. Missing values,
# e. Variable types.
# 3. Create new variables for each customer's total number of purchases and spending, considering OmniChannel purchases.
# 4. Examine variable types. Convert variables representing dates to the date format.
# 5. Explore the distribution of the number of customers, average number of products purchased, and average spending in different purchase channels.
# 6. Rank the top 10 customers with the highest revenue.
# 7. Rank the top 10 customers with the highest number of orders.
# 8. Modularize the data preprocessing process.

data = pd.read_csv("flo_data_20k.csv")  # 1
# 2
print(data.head(10))  # a data[:10] but .head(10) is more readable
print(data.columns)  # b
print(data.describe())  # c
print(data[data.isnull()])  # d
print(data.dtypes)  # d dtypes is attribute so we dont use '()' when we call this

# TASK 2: Calculation of RFM Metrics
current_date = pd.to_datetime('now')
data['last_order_date'] = pd.to_datetime(data['last_order_date'])

data['recency'] = current_date - data['last_order_date']
data['frequency'] = data['order_num_total_ever_online'] + data['order_num_total_ever_offline']
data['monetary'] = data['customer_value_total_ever_offline'] + data['customer_value_total_ever_online']

# TASK 3: Calculation of RF and RFM Scores
data['recencyScore'] = pd.cut(data['recency'], bins=5, labels=[5, 4, 3, 2, 1]).astype(str)
data['frequencyScore'] = pd.cut(data['frequency'], bins=5, labels=[1, 2, 3, 4, 5]).astype(str)
data['monetaryScore'] = pd.cut(data['monetary'], bins=5, labels=[1, 2, 3, 4, 5]).astype(str)

data['RF'] = data['recencyScore'] + data['frequencyScore']
data['RFM'] = data['RF'] + data['monetaryScore']

# TASK 4: Definition of RF Scores as Segments
seg_map = {
    r'[1-2][1-2]': 'hibernating',
    r'[1-2][3-4]': 'at_risk',
    r'[1-2]5': 'cant_lose',
    r'3[1-2]': 'about_to_sleep',
    r'33': 'need_attention',
    r'[3-4][4-5]': 'loyal_costumer',
    r'41': 'promising',
    r'51': 'new_costumers',
    r'[4-5][2-3]': 'potential_loyalist',
    r'5[4-5]': 'champions'
}

# TASK 5: Action Time!
# 1. Examine the averages of recency, frequency, and monetary values for each segment.
# 2. Find customers matching the profiles for 2 cases using RFM analysis and save their customer IDs to a CSV file.
# a. FLO is introducing a new women's shoe brand. The brand's product prices are higher than the general customer preferences. Therefore, FLO wants to communicate
# and establish a connection with loyal customers (champions, loyal customers) who have an average spending above 250 TL and shop in the women's category. Save the customer IDs
# to a CSV file named new_brand_target_customer_ids.csv.
# b. A discount of nearly 40% is planned for men's and children's products. FLO wants to target customers interested in these categories who were good customers in the past
# but haven't shopped for a long time, new customers, and those who are currently inactive. Save the customer IDs to a CSV file named discount_target_customer_ids.csv.

# TASK 6: Modularize the Entire Process

###############################################################
# TASK 1: Data Understanding and Preparation
###############################################################


# 2. In the dataset,
# a. First 10 observations,
# b. Variable names,
# c. Dimension,
# d. Descriptive statistics,
# e. Missing values,
# f. Variable types.


# 3. OmniChannel customers shop both online and offline.
# Create new variables for each customer's total number of purchases and spending.


# 4. Examine variable types. Convert variables representing dates to the date format.


# df["last_order_date"] = df["last_order_date"].apply(pd.to_datetime)


# 5. Explore the distribution of the number of customers, average number of products purchased, and average spending in different purchase channels.


# 6. Rank the top 10 customers with the highest revenue.


# 7. Rank the top 10 customers with the highest number of orders.


# 8. Modularize the data preprocessing process.


###############################################################
# TASK 2: Calculation of RFM Metrics
###############################################################

# Analysis date is 2 days after the date of the last purchase made in the dataset.


# Create a new RFM dataframe with customer_id, recency, frequency, and monetary values.


###############################################################
# TASK 3: Calculation of RF and RFM Scores
###############################################################

# Convert Recency, Frequency, and Monetary metrics into scores ranging from 1 to 5 using qcut,
# and save these scores as recency_score, frequency_score, and monetary_score.


# Represent recency_score and frequency_score as a single variable and save it as RF_SCORE.


###############################################################
# TASK 4: Definition of RF Scores as Segments
###############################################################

# Define segments for the created RFM scores to make them more understandable,
# and convert RF_SCORE into segments using the defined seg_map.


###############################################################
# TASK 5: Action Time!
###############################################################

# 1. Examine the averages of recency, frequency, and monetary values for each segment.


# 2. Using RFM analysis, find customers matching the profiles for 2 cases.
# Save their customer IDs to a CSV file.

# a. FLO is introducing a new women's shoe brand with higher prices than average customer preferences. FLO wants to communicate
# and establish a connection with loyal customers (champions, loyal customers) who have an average spending above 250 TL and shop in the women's category.
# Save the customer IDs to a CSV file named new_brand_target_customer_ids.csv.


# b. A discount of nearly 40% is planned for men's and children's products. FLO wants to target customers interested in these categories who were good customers in the past
# but haven't shopped for a long time, new customers, and those who are currently inactive.
# Save the customer IDs to a CSV file named discount_target_customer_ids.csv.


# TASK 6: Modularize the Entire Process
