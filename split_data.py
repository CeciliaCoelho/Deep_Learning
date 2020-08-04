import sklearn.model_selection as model_selection
import csv

X = []
y = []

with open("C:/Users/Cecilia/Desktop/code/Pets_Classifier/annotations/csv/annotations.csv" , 'r') as fr:
    lines = csv.reader(fr, delimiter=',')
    for row in lines:
        X.append(row[0])
        y.append(row[1:])

X_train, X_test , y_train , y_test = model_selection.train_test_split(X, y , train_size=0.80,test_size=0.20, random_state=101)


with open("train_labels.csv" , "a") as tr:
    for i,j in zip(X_train, y_train):
        tr.write(",".join([i , str(j)]))
        tr.write("\n")

with open("test_labels.csv" , "a") as tr:
    for a,b in zip(X_test, y_test):
        tr.write(",".join([a , str(b)]))
        tr.write("\n")