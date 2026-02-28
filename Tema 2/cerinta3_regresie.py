import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
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

clf = LogisticRegression(
    penalty='l2',            # Regularizare L2 (Ridge)
    solver='saga',          # Optimizator folosit
    C=1.0,                   # Inversul regularizarii (default = 1.0)
    max_iter=1000,           # Numar max de iteratii
    class_weight='balanced', # Ajusteaza automat greutatile claselor
    multi_class='multinomial',
    random_state=42
)

clf.fit(X_train, y_train)

# 6. EVALUARE
y_pred = clf.predict(X_test)

print("Acuratete:", accuracy_score(y_test, y_pred))
print("\nMatrice de confuzie:\n", confusion_matrix(y_test, y_pred))
print("\nRaport clasificare:\n", classification_report(y_test, y_pred, target_names=label_encoder.classes_))
