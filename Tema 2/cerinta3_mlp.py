import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import LabelEncoder
import cerinta2

# 1. CITIRE DATE
df = pd.read_csv("pirvision_office_train.csv")
df = cerinta2.preProcessingData(df)

# 2. SEPARARE X / y
target_column = 'Day'
y = df[target_column]
X = df.drop(columns=[target_column])

# 3. ENCODARE
categorical_cols = X.select_dtypes(include=['object', 'category', 'bool']).columns
X = pd.get_dummies(X, columns=categorical_cols)  # One-hot encoding pentru X

label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# 4. ÎMPĂRȚIRE ÎN TRAIN/TEST
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. MODEL MLP
mlp = MLPClassifier(
    hidden_layer_sizes=(100, 50),     # două straturi ascunse: 100 și 50 neuroni
    activation='relu',                # funcție de activare: ReLU
    solver='adam',                    # optimizator: Adam
    learning_rate_init=0.001,         # learning rate inițial
    max_iter=200,                     # număr maxim de epoci
    batch_size=64,                    # dimensiunea batch-urilor
    early_stopping=True,              # regularizare: oprire timpurie
    alpha=0.0001,                     # regularizare L2
    random_state=42
)

mlp.fit(X_train, y_train)

# 6. EVALUARE
y_pred = mlp.predict(X_test)

print("Acuratete:", accuracy_score(y_test, y_pred))
print("\nMatrice de confuzie:\n", confusion_matrix(y_test, y_pred))
print("\nRaport clasificare:\n", classification_report(y_test, y_pred, target_names=label_encoder.classes_))
