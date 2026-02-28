import pandas as pd

# CITIRE FISIER CSV
file_name = "pirvision_office_train.csv"
df = pd.read_csv(file_name)

# TIPURI DATE
print(df.info())

# SELECTARE COLOANE NUMERICE
numerice = df.select_dtypes(include=['float64', 'int64'])

# CALCULARE DATE STATISTICE (NR. DE EXEMPLE, MEDIA, DEVIATIA STANDARD ETC.)
stats = numerice.describe(percentiles=[.25, .50, .75]).transpose() 
stats['missing'] = df[numerice.columns].isnull().sum() # ADAUGARE COLOANA VALORI LIPSA
print(stats)

import seaborn as sns
import matplotlib.pyplot as plt

# HISTOGRAME COLOANE
for col in numerice.columns:
    plt.figure(figsize=(6, 1.5))
    sns.boxplot(x=df[col])
    plt.title(f'{col}')
    plt.show()

# SELECTARE COLOANE CATEGORICE(DISCRETE/ORDINALE)
categorice = df.select_dtypes(include=['object', 'category'])

# CALCULARE DATE STATISTICE(NR.VALORI UNICE, NR.VALORI LIPSA)
for col in categorice.columns:
    print(f"{col}:")
    print(f"- Valori unice: {df[col].nunique()}")
    print(f"- Valori lipsa: {df[col].isnull().sum()}")

# HISTOGRAMA COLOANE
for col in categorice.columns:
    plt.figure(figsize=(6, 4))
    sns.countplot(x=col, data=df)
    plt.title(f'Distribuția valorilor pentru {col}')
    plt.xticks(rotation=45)
    plt.show()

# ANALIZA ECHILIBRULUI DE CLASE
col = categorice.columns[0] # EXEMPLU
sns.countplot(x=col, data=df)
plt.title(f'Analiza echilibrului de clase pentru {col}')
plt.show()

# ANALIZA CORELATIEI INTRE ATRIBUTE NUMERICE
corr = df.corr(numeric_only=True)

plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Corelația dintre atributele numerice")
plt.show()
