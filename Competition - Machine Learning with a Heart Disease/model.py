# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 17:47:58 2019

@author: sumit.dubey
"""

import pandas as pd
import util
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier 
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import Imputer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.ensemble import RandomForestClassifier

pd.set_option('display.max_columns', 500)

dummies_cols = ['slope_of_peak_exercise_st_segment','thal','chest_pain_type','sex','exercise_induced_angina']
#dummies_cols = ['slope_of_peak_exercise_st_segment','thal']
categorize_label = lambda x: x.astype('category')

df_test_labels = pd.read_csv('submission_format.csv')
df_test_values = pd.read_csv('test_values.csv')
df_train_labels = pd.read_csv('train_labels.csv')
df_train_values = pd.read_csv('train_values.csv')

train_df = pd.read_csv('train_values.csv')
test_df =  pd.read_csv('test_values.csv')                


df_train_values[dummies_cols]=df_train_values[dummies_cols].apply(categorize_label,axis=0)
df_train_values = pd.concat([df_train_values,pd.get_dummies(df_train_values[dummies_cols])],axis=1)
df_train_values.drop(columns=dummies_cols,inplace=True)
df_train = pd.merge(left= df_train_values,right = df_train_labels,on='patient_id')

x_train = df_train.drop(['patient_id','heart_disease_present'],axis=1).astype(float)
y_train = df_train['heart_disease_present']
print('x_train->',x_train.info())

df_test_values[dummies_cols]=df_test_values[dummies_cols].apply(categorize_label,axis=0)
df_test_values = pd.concat([df_test_values,pd.get_dummies(df_test_values[dummies_cols])],axis=1)
df_test_values.drop(columns=dummies_cols,inplace=True)
df_test = pd.merge(left= df_test_values,right = df_test_labels,on='patient_id')

x_test = df_test.drop(['patient_id','heart_disease_present'],axis=1).astype(float)
y_test = df_test['heart_disease_present']
print('X_test->',x_test.info())

reg = Pipeline([
        ('scaler', StandardScaler()),
        ('reg', LogisticRegression())
        ])

knn = Pipeline([
        ('scaler', StandardScaler()),
        ('knn', KNeighborsClassifier(n_neighbors=180))
        ])


pl = Pipeline([
        ('scaler', StandardScaler()),
        ('clf', OneVsRestClassifier(LogisticRegression()))
        ])

pl_random = Pipeline([
        ('scaler', StandardScaler()),
        ('clf', OneVsRestClassifier(RandomForestClassifier()))
        ])

#reg = LogisticRegression()
#knn = KNeighborsClassifier(n_neighbors=180)
dtc = DecisionTreeClassifier()


reg.fit(x_train,y_train)
knn.fit(x_train,y_train)
dtc.fit(x_train,y_train)
pl.fit(x_train,y_train)
pl_random.fit(x_train,y_train)


y_test_predicted= reg.predict_proba(x_test)[:,1]
y_test_predicted_knn= knn.predict_proba(x_test)[:,1]
y_test_predicted_dtc= dtc.predict_proba(x_test)[:,1]
y_test_predicted_pl= pl.predict_proba(x_test)[:,1]
y_test_predicted_pl_random= pl_random.predict_proba(x_test)[:,1]


# preparing data for submission --- LogisticRegression
df_test_labels.drop(columns=['heart_disease_present'],inplace=True)
df_test_labels['heart_disease_present'] = y_test_predicted
df_test_labels.to_csv('submission_reg.csv', index=False)

# preparing data for submission --- KNeighborsClassifier
df_test_labels.drop(columns=['heart_disease_present'],inplace=True)
df_test_labels['heart_disease_present'] = y_test_predicted_knn
df_test_labels.to_csv('submission_knn.csv', index=False)

#print('y_test_predicted-->',type(y_test_predicted))
#print('y_test_predicted-->',y_test_predicted)
#print('y_test-->',type(y_test.values))
#print('y_test-->',y_test.values)
logloss= util.compute_log_loss(y_test_predicted,y_test)
print('logloss--->',logloss)
logloss_knn= util.compute_log_loss(y_test_predicted_knn,y_test)
print('logloss_knn--->',logloss_knn)
logloss_dtc= util.compute_log_loss(y_test_predicted_dtc,y_test)
print('logloss_dtc--->',logloss_dtc)
logloss_pl= util.compute_log_loss(y_test_predicted_pl,y_test)
print('logloss_pl--->',logloss_pl)
logloss_pl_random= util.compute_log_loss(y_test_predicted_pl_random,y_test)
print('logloss_pl_random--->',logloss_pl_random)

#predict_score =reg.score(X_test,y_test.values)
#print('score id -->',predict_score)





