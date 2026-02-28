import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import cerinta2

# 1. CITIRE SI PREPROCESARE
df = pd.read_csv("pirvision_office_train.csv")
df = cerinta2.preProcessingData(df)

# 2. SEPARARE VARIABILA TINTA SI PREDICTORI
target_col = 'Day'  # Inlocuieste cu numele real al coloanei tinta
X = df.drop(columns=[target_col])
y = df[target_col]

# 3. ENCODE TARGET CU LabelEncoder
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# 4. ENCODE VARIABILE CATEGORICE CU get_dummies
X_encoded = pd.get_dummies(X, drop_first=True)

# 5. IMPARTIRE SETURI
X_train, X_test, y_train, y_test = train_test_split(
    X_encoded, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded
)

# 6. ANTRENARE MODEL 
clf = DecisionTreeClassifier(
    criterion='gini',
    max_depth=5,
    min_samples_leaf=3,
    class_weight='balanced',
    random_state=42
)

clf.fit(X_train, y_train)

# 7. EVALUARE
y_pred = clf.predict(X_test)

print("Acuratete:", accuracy_score(y_test, y_pred))
print("\nMatrice de confuzie:\n", confusion_matrix(y_test, y_pred))
print("\nRaport clasificare:\n", classification_report(y_test, y_pred, target_names=label_encoder.classes_))
