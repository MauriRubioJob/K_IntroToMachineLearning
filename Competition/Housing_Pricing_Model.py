# https://www.kdnuggets.com/2016/11/rank-ten-precent-first-kaggle-competition.html

# Import all that I need
import pandas as pd
import matplotlib as mpl
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

# Load the data from the directoory
data_path = "Competition/input/train.csv"
data = pd.read_csv(data_path)
# print(data.describe)  # In order to get some statistic info about it
print(data.dtypes.sample(30))
data = pd.get_dummies(data)
print(data.dtypes.sample(30))
# EDA (Exploratory Data Analysis)
# https://www.kaggle.com/code/pmarcelino/comprehensive-data-exploration-with-python



# Get the target and store it in y. In this case the target from which we are going ton learn, and predict is the SalePrice of the house.
# print(data.columns)  #So we Know the names of the columns.
y = data["SalePrice"]

# Select some Features to  build the model around.
# features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
# features = ['LotArea', 'YearBuilt', '1stFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd', 'Neighborhood', 'PoolQC']

# X = data[features]
