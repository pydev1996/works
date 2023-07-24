# Importing Libraries:
import pandas as pd
import numpy as np
import pickle
from sklearn.metrics import accuracy_score, confusion_matrix

# for displaying all feature from dataset:
pd.pandas.set_option('display.max_columns', None)

# Reading Dataset:
dataset = pd.read_csv("Dataset/Liver_data.csv")

# Filling NaN Values of "Albumin_and_Globulin_Ratio" feature with Median:
dataset['Albumin_and_Globulin_Ratio'] = dataset['Albumin_and_Globulin_Ratio'].fillna(dataset['Albumin_and_Globulin_Ratio'].median())

# Label Encoding:
dataset['Gender'] = np.where(dataset['Gender']=='Male', 1,0)

# Droping 'Direct_Bilirubin' feature:
dataset = dataset.drop('Direct_Bilirubin', axis=1)

# Independent and Dependent Feature:
X = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1]

# SMOTE Technique:
from imblearn.combine import SMOTETomek
smote = SMOTETomek()
X_smote, y_smote = smote.fit_resample(X,y)

# Train Test Split:
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X_smote,y_smote, test_size=0.3, random_state=33)

# RandomForestClassifier:
from sklearn.ensemble import RandomForestClassifier
RandomForest = RandomForestClassifier()
RandomForest = RandomForest.fit(X_train,y_train)
y_pred1 = RandomForest.predict(X_test)
print("RandomForest",accuracy_score(y_test, y_pred1))

from sklearn.svm import SVC
svc = SVC(kernel='linear',probability=True)

svc.fit(X_train, y_train)
y_pred2 = svc.predict(X_test)
print("SVM Classifier",accuracy_score(y_test, y_pred2))

from sklearn.naive_bayes import GaussianNB  
nb = GaussianNB()
nb.fit(X_train, y_train)
y_pred3 = nb.predict(X_test)
print("NaiveBayes Classifier",accuracy_score(y_test, y_pred3))


#Creating a pickle file for the classifier
filename = 'Liver2.pkl'
pickle.dump(RandomForest, open(filename, 'wb'))