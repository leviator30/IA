import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
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
clf = RandomForestClassifier(
    n_estimators=100,          # numărul de arbori
    max_depth=15,              # adancimea maxima a unui arbore
    min_samples_leaf=5,        # numar minim de exemple într-o frunza
    criterion='entropy',       # functia de decizie: 'gini', 'entropy', 'log_loss'
    class_weight='balanced',   # ponderare automata a claselor
    max_samples=0.8,           # 80% din date pentru fiecare estimator
    max_features='sqrt',       # radacina nr. total de atribute (proportia de atribute)
    random_state=42
)

clf.fit(X_train, y_train)

# 6. EVALUARE
y_pred = clf.predict(X_test)

print("Acuratete:", accuracy_score(y_test, y_pred))
print("\nMatrice de confuzie:\n", confusion_matrix(y_test, y_pred))
print("\nRaport clasificare:\n", classification_report(y_test, y_pred, target_names=label_encoder.classes_))