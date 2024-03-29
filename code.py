
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
import statistics
import math

df = pd.read_csv("CAR DETAILS.csv")
df.head(5)     # Top 5 rows

# Checking the datatypes of the columns
df.dtypes

# Checking the shape of the dataset
df.shape

# Checking the Column Names
df.columns


# Checking the Null values
df.isnull().sum()

#### **Checking the duplicate values (Data Cleaning)**

df.duplicated().sum()

# Description of the numerical columns
df.describe()

# Description of all the columns
df.describe(include = "all")

# Short Information of all the columns
df.info()

print('Categorical Data: ')

print('Fuel unique values: ', df['fuel'].unique())
print('Number of unique values: ', df['fuel'].unique().size)

print('Seller type unique values: ', df['seller_type'].unique())
print('Number of unique values: ', df['seller_type'].unique().size)

print('Transmission unique values: ', df['transmission'].unique())
print('Number of unique values: ', df['transmission'].unique().size)

print('Owner unique values: ', df['owner'].unique())
print('Number of unique values: ', df['owner'].unique().size)

# Unique number of Cars
df["name"].nunique()

name = df["name"].str.split(" ", expand = True)
df["car_maker"] = name[0]
df["car_model"] = name[1]

print("Data after splitting car names")
df.head()

df["current_year"] = 2023

df["no_of_total_years"] = df["current_year"]-df["year"]
df.drop(["current_year"], axis = 1, inplace = True)
df.head()

df.drop(["name"], inplace = True, axis = 1)
df.head()

cat_col = df.select_dtypes(include = "object").columns
print("Categorical Columns:",cat_col)
num_col = df.select_dtypes(exclude = "object").columns
print("Numerical Columns:",num_col)

# Value Counts of Categorical Columns
a2 = df["fuel"].value_counts()
a3 = df["seller_type"].value_counts()
a4 = df["transmission"].value_counts()
a5 = df["owner"].value_counts()
a6 = df["car_maker"].value_counts()
a7 = df["car_model"].value_counts()

print('Fuel unique values:\n', a2,"\n")
print('Seller type unique values:\n', a3,"\n")
print('Transmission unique values:\n', a4,"\n")
print('Owner unique values:\n', a5,"\n")
print('Car Maker unique values:\n', a6,"\n")
print('Car Model unique values:\n', a7,"\n")

figure, axis = plt.subplots(3,2, figsize = (12,17))

axis[0,0].barh(a5.index, a5.values, color = "red", edgecolor = "Black")
axis[0,0].legend
axis[0,0].set_title("Owner Count")

axis[0,1].bar(a3.index, a3.values, color = "orange", edgecolor = "Black")
axis[0,1].legend
axis[0,1].set_title("Seller Type Count")

axis[1,0].bar(a4.index, a4.values, color = "green", edgecolor = "Black")
axis[1,0].legend
axis[1,0].set_title("Transmission Type Count")

axis[1,1].bar(a2.index, a2.values, color = "cyan", edgecolor = "Black")
axis[1,1].legend
axis[1,1].set_title("Fuel Type Count")

axis[2,0].barh(a6.index, a6.values, color = "green", edgecolor = "Black")
axis[2,0].legend
axis[2,0].set_title("Car Maker Type Count")

plt.show()

#### Scatter plots of numerical columns
# Checking the column names
df.columns

figure, (ax1, ax2) = plt.subplots(1,2, figsize = (10,3))

ax1.scatter(df.year, df["selling_price"], color = "lightblue", marker = "*")
ax1.set_title("year vs selling_price")

ax2.scatter(df.year, df["km_driven"], color = "lightgreen", marker = "o")
ax2.set_title("year vs km_driven")

plt.show()

# Checking the categorical column names
cat_col

figure, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2, figsize = (10,5))

ax1.pie(a2.values, labels = a2.index, autopct = "%.2f%%")
ax1.legend(bbox_to_anchor = (1,1,0.4,0))
ax1.set_title("Fuel Count Percentage Distribution")

ax2.pie(a3.values, labels = a3.index, autopct = "%.2f%%")
ax2.legend(bbox_to_anchor = (1,1,0.4,0))
ax2.set_title("Seller_type Count Percentage Distribution")

ax3.pie(a4.values, labels = a4.index, autopct = "%.2f%%")
ax3.legend(bbox_to_anchor = (1,1,0.4,0))
ax3.set_title("Transmission Count Percentage Distribution")

ax4.pie(a5.values, labels = a5.index, autopct = "%.2f%%")
ax4.legend(bbox_to_anchor = (1,1,2,0))
ax4.set_title("Owner Count Percentage Distribution")

plt.show()

print(cat_col)
print(num_col)

plt.figure(figsize = (12,10))
sns.boxplot(y = df["car_maker"], x = df.selling_price)
plt.ylabel("Car Maker")
plt.title("Car Maker based on Selling Price - Boxplot")
plt.show()

plt.figure(figsize = (12,10))
sns.boxplot(x = df.km_driven, y = df["car_maker"])
plt.ylabel("Car Maker")
plt.title("car_maker based on Km driven - Boxplot")
plt.xticks(rotation = 90)
plt.show()

plt.figure(figsize = (12,10))
sns.boxplot(x = df["year"], y = df.fuel)
plt.ylabel("Fuel Type")
plt.title("Fuel based on Year - Boxplot")
plt.show()

plt.figure(figsize = (12,10))
sns.boxplot(x = df["year"], y = df.seller_type)
plt.ylabel("Seller Type")
plt.title("Seller type based on Year - Boxplot")
plt.show()

#### **Violin Plot**

print(cat_col)
print(num_col)

plt.figure(figsize = (12,10))
sns.violinplot(x = df["year"], y = df.transmission)
plt.ylabel("Transmission Type")
plt.title("Transmission based on Year - Violin plot")
plt.show()

plt.figure(figsize = (12,10))
sns.violinplot(x = df["year"], y = df.owner)
plt.ylabel("Ownership")
plt.title("Owner based on Year - Violin plot")
plt.show()

#### **Pair plots of Numerical Columns**

df.columns

sns.pairplot(data = df, vars = ['year', 'selling_price', 'km_driven', "no_of_total_years"])
plt.show()

corr = df.corr()
corr

sns.heatmap(corr, annot = True, cmap = "coolwarm")
plt.title("Correlation of Numerical columns")
plt.show()

df.drop("year", axis = 1, inplace = True)

# **Encoding the Data (Data Preprocessing)**

#### **Make a copy of dataframe**
# Make a copy of dataframe
df1 = df.copy()
df1.head()

df1.shape

# Encoding data with get dummies
df1 = pd.get_dummies(df1, drop_first=True, columns = ["car_maker", "car_model"])
df1.head()

# Checking the shape of the encoded data
df1.shape

# Checking the datatypes of the encoded data
df1.dtypes

# Importing the libraries for encoding
from sklearn.preprocessing import LabelEncoder

# Check the columns which we want to encode
cat_col

# Creating an object of LabelEncoder
le = LabelEncoder()

# Creating a for loop for Encoding multiple columns
encoded_columns = ['fuel', 'seller_type', 'transmission', 'owner']

for i in encoded_columns:
  df1[i] = le.fit_transform(df1[i])


df1.head()

x = df1.drop("selling_price", axis = 1)
y = df1.selling_price
print(x.shape)
print(y.shape)

# Importing Libraries for splitting data into Training and Testing
from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size = .20, random_state = 0)
print(xtrain.shape)
print(xtest.shape)
print(ytrain.shape)
print(ytest.shape)

# we can check our Test data is correct
4340*.25

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Creating functions for evaluating scores
def scores(ytest, ypred):
  mae = mean_absolute_error(ytest, ypred)
  mse = mean_squared_error(ytest, ypred)
  rmse = np.sqrt(mean_squared_error(ytest, ypred))
  r2 = r2_score(ytest, ypred)
  print("MAE: ", mae)
  print("MSE: ", mse)
  print("RMSE: ", rmse)
  print("R2 Score: ", r2)

def model_score(model):
  print("Training Score: ", model.score(xtrain, ytrain))
  print("Testing Score: ", model.score(xtest, ytest))

def adjusted_r2_score(ytest, y_pred, n_features):
    r_squared = r2_score(ytest, y_pred)
    adjusted_r_squared = 1 - (1 - r_squared) * (len(ytest) - 1) / (len(ytest) - n_features - 1)
    print("Adjusted R2 Score: ", adjusted_r_squared)

from sklearn.linear_model import LinearRegression,Ridge,Lasso
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import accuracy_score
from sklearn.ensemble import BaggingClassifier, BaggingRegressor

### **1) Linear Regression**"""

lr = LinearRegression()
lr.fit(xtrain, ytrain)

model_score(lr)

ypred_lr = lr.predict(xtest)
ypred_lr

scores(ytest, ypred_lr)

adjusted_r2_score(ytest, ypred_lr, (df1.shape[1]-1))

### **2) Ridge Regression**"""

rr = Ridge(alpha=25)
rr.fit(xtrain, ytrain)

model_score(rr)

ypred_rr = rr.predict(xtest)
ypred_rr

scores(ytest, ypred_rr)

adjusted_r2_score(ytest, ypred_rr, (df1.shape[1]-1))

"""### **3) Lasso Regression**"""

lar = Lasso(alpha=0.1)
lar.fit(xtrain, ytrain)

model_score(lar)

ypred_lar = lar.predict(xtest)
ypred_lar

scores(ytest, ypred_lar)

adjusted_r2_score(ytest, ypred_lar, (df1.shape[1]-1))

"""### **4) KNeighborsRegressor**"""

knn = KNeighborsRegressor(n_neighbors = 15)
knn.fit(xtrain, ytrain)

model_score(knn)

ypred_knn = knn.predict(xtest)
ypred_knn

scores(ytest, ypred_knn)

adjusted_r2_score(ytest, ypred_knn, (df1.shape[1]-1))

"""### **5) Decision Tree Regression**"""

dtr = DecisionTreeRegressor(random_state = 7, max_depth=4)
dtr.fit(xtrain, ytrain)

model_score(dtr)

 

ypred_dtr = dtr.predict(xtest)
ypred_dtr

 

scores(ytest, ypred_dtr)

adjusted_r2_score(ytest, ypred_dtr, (df1.shape[1]-1))

"""### **6) Bagging Regressor with Decision Tree Regression**"""

bag_dtr = BaggingRegressor(estimator = dtr, n_estimators = 15,
                              max_samples = xtrain.shape[0],
                            max_features = xtrain.shape[1],
                           random_state = 7)
bag_dtr.fit(xtrain, ytrain)

 

model_score(bag_dtr)

 

ypred_bag_dtr = bag_dtr.predict(xtest)
ypred_bag_dtr

 

scores(ytest, ypred_bag_dtr)

adjusted_r2_score(ytest, ypred_bag_dtr, (df1.shape[1]-1))

"""### **7) Bagging Regressor with Linear Regression**"""

bag_lr = BaggingRegressor(estimator = lr, n_estimators = 15,
                              max_samples = xtrain.shape[0],
                          max_features = xtrain.shape[1],
                          random_state = 7)
bag_lr.fit(xtrain, ytrain)


model_score(bag_lr)

 

ypred_bag_lr = bag_lr.predict(xtest)
ypred_bag_lr

 

scores(ytest, ypred_bag_lr)

adjusted_r2_score(ytest, ypred_bag_lr, (df1.shape[1]-1))

"""# **Checking Errors using Plots**"""

# Creating variables for plotting errors
error_lr = [i for i in range(len(ypred_lr))]
error_rr = [i for i in range(len(ypred_rr))]
error_lar = [i for i in range(len(ypred_lar))]
error_knn = [i for i in range(len(ypred_knn))]
error_dtr = [i for i in range(len(ypred_dtr))]
error_bag_dtr = [i for i in range(len(ypred_bag_dtr))]
error_bag_lr = [i for i in range(len(ypred_bag_lr))]

figure, ((ax1, ax2, ax3), (ax4, ax5, ax6), (ax7, ax8, ax9)) = plt.subplots(3,3, figsize = (15,12))

ax1.plot(error_lr, ytest-ypred_lr)
ax1.set_title("Error in Linear Regression")

ax2.plot(error_rr, ytest-ypred_rr)
ax2.set_title("Error in Ridge Regression")

ax3.plot(error_lar, ytest-ypred_lar)
ax3.set_title("Error in Lasso Regression")

ax4.plot(error_knn, ytest-ypred_knn)
ax4.set_title("Error in KNeighbors Regression")

ax5.plot(error_dtr, ytest-ypred_dtr)
ax5.set_title("Error in Decision Tree Regression")

ax6.plot(error_bag_dtr, ytest-ypred_bag_dtr)
ax6.set_title("Error in Bagging Decision Tree Regression")

ax7.plot(error_bag_lr, ytest-ypred_bag_lr)
ax7.set_title("Error in Bagging Linear Regression")


plt.show()

"""# **Creating Dataframe of Models Score**"""

all_model = {"Linear Reg":[mean_absolute_error(ytest, ypred_lr), mean_squared_error(ytest, ypred_lr), np.sqrt(mean_squared_error(ytest, ypred_lr)), r2_score(ytest, ypred_lr), 0.8140642789717978],
             "Ridge Reg":[mean_absolute_error(ytest, ypred_rr), mean_squared_error(ytest, ypred_rr), np.sqrt(mean_squared_error(ytest, ypred_rr)), r2_score(ytest, ypred_rr), 0.6819590923562783],
             "Lasso Reg":[mean_absolute_error(ytest, ypred_lar), mean_squared_error(ytest, ypred_lar), np.sqrt(mean_squared_error(ytest, ypred_lar)), r2_score(ytest, ypred_lar), 0.8151527670364602],
             "KNeighbors Reg":[mean_absolute_error(ytest, ypred_knn), mean_squared_error(ytest, ypred_knn), np.sqrt(mean_squared_error(ytest, ypred_knn)), r2_score(ytest, ypred_knn), 0.3046351810084197],
             "Decision Tree Reg":[mean_absolute_error(ytest, ypred_dtr), mean_squared_error(ytest, ypred_dtr), np.sqrt(mean_squared_error(ytest, ypred_dtr)), r2_score(ytest, ypred_dtr), 0.5413406772377228],
             "Bagging with Decision Tree Reg":[mean_absolute_error(ytest, ypred_bag_dtr), mean_squared_error(ytest, ypred_bag_dtr), np.sqrt(mean_squared_error(ytest, ypred_bag_dtr)), r2_score(ytest, ypred_bag_dtr), 0.6277991900261446],
             "Bagging with Linear Reg":[mean_absolute_error(ytest, ypred_bag_lr), mean_squared_error(ytest, ypred_bag_lr), np.sqrt(mean_squared_error(ytest, ypred_bag_lr)), r2_score(ytest, ypred_bag_lr), 0.8112635600586408]}

res = pd.DataFrame(all_model, index = ["MAE", "MSE", "RMSE", "R2 Score", "Adjusted R2 Score"])
res

model = Lasso(alpha=0.1)
model.fit(x, y)


ypred = model.predict(x)
ypred


scores(y, ypred)

model_score(model)

adjusted_r2_score(y, ypred, (df1.shape[1]-1))

"""# **Importing Pickle Library for Saving and Loading Model**"""

import pickle

"""# **Saving the best model using Pickle**"""

pickle.dump(model,open('best_model.pkl','wb'))

"""
# **Collecting 20 Datapoints randomly from our dataset**"""

df_20 = df1.sample(20)
df_20.head()

# Saving the Sample Dataset
df_20.to_csv("sample_dataset.csv")

"""#### **Selecting Dependent and Independent Variable for randomly 20 points selecting dataset**"""

x_20 = df_20.drop("selling_price", axis = 1)
y_20 = df_20["selling_price"]
print(x.shape)
print(y.shape)

"""#### **Splitting the data into Training and Testing for randomly 20 points selecting dataset**"""

xtrain_20, xtest_20, ytrain_20, ytest_20 = train_test_split(x, y, test_size = .25)
print(xtrain_20.shape)
print(ytrain_20.shape)
print(xtest_20.shape)
print(ytest_20.shape)

"""#### **Loading the best model using Pickle**"""

# Load the saved trained ML model
best_model_20 = pickle.load(open("/content/best_model.pkl", "rb"))
best_model_20

"""#### **Generate the Predictions for randomly 20 points selecting dataset**"""

ypred_20 = best_model_20.predict(xtest_20)
ypred_20

"""#### **Checking the Scores for randomly 20 points selecting dataset**"""

model_score(best_model_20)

scores(ytest_20, ypred_20)

adjusted_r2_score(ytest_20, ypred_20, (df_20.shape[1]-1))

"""# **Making Pipelines**

#### **Importing Libraries for Pipelines**
"""

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import Lasso

# Extract Categorical Columns
categorical_cols = ['fuel', 'seller_type', 'transmission', 'owner', 'car_maker', 'car_model']

"""#### **Splitting data into Training and Testing**"""

X = df.drop("selling_price", axis = 1)
Y = df["selling_price"]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.35, random_state=7)
print(X_train.shape)
print(Y_train.shape)
print(X_test.shape)
print(Y_test.shape)

# One Hot Encoding
preprocessor = ColumnTransformer([
    ("OneHotEncoding", OneHotEncoder(sparse = False, handle_unknown = "ignore"), categorical_cols)
    ], remainder = "passthrough")

"""# **Create Pipelines**"""

# Create Pipeline Object with best fit model
lasso = Lasso(alpha = 0.1, max_iter = 1000)
pipeline = Pipeline(steps = [("Preprocessor", preprocessor), ("model", lasso)], verbose = True)
pipeline

"""#### **Train the model**"""

# Fitting the model
pipeline.fit(X, Y)

"""#### **Generate the predictions**"""

# Generate the predictions
pipe_pred = pipeline.predict(X_test)
pipe_pred

"""#### **Checking the score**"""

# Checking the R2 Score
r2_score(Y_test, pipe_pred)

# Checking the Adjusted R2 Score
adjusted_r2_score(Y_test, pipe_pred, (df.shape[1]-1))

"""# **Saving the pipeline model for using in Web App**"""

pickle.dump(pipeline,open('pipeline_model.pkl','wb'))