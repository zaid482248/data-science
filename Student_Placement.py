import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from mlxtend.plotting import plot_decision_regions



df = pd.read_csv(r"D:\Data Science\data\Placement.csv")


# print(df.head()) 
# print(df.info())
# print(df.describe())
# print(df.isnull().sum())
# print(df.shape)


df.drop_duplicates(inplace=True)
# df.drop(columns=["Unnamed: 0"] , axis=1 , inplace=True)
# df = df.drop(columns=["Unnamed"] , axis=1)


df = df.iloc[:,1:]

# # plt.scatter(df["cgpa"] , df["iq"] , c = df["placement"])
# plt.xlabel("CGPA")
# plt.ylabel("IQ")
# plt.title("Placement based on CGPA and IQ")
# plt.tight_layout()
# plt.show()
# print(df.head())

X_independent = df.iloc[:,0:2]
Y_dependent = df.iloc[:,-1]

# print(X_independent)
# print(Y_dependent)

X_train , X_test ,Y_train , Y_test = train_test_split(X_independent , Y_dependent , test_size= 0.1 , random_state=2)

# print(X_train.shape , X_test.shape)
# print(Y_train.shape , Y_test.shape)


scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)

x_test = scaler.transform(X_test)
# print(X_train)


logic = LogisticRegression()

logic.fit(X_train , Y_train)

logic.predict(X_test)


# print(f"Model Accuracy is {logic.score(X_test , Y_test)*100} %") 

accuracy_score(Y_test , logic.predict(X_test))


print("prediction of this model is " , accuracy_score(Y_test , logic.predict(X_test))*100 , "%")

 

plot_decision_regions(X_train , Y_train.values , clf=logic , legend=2)

plt.show()
 



