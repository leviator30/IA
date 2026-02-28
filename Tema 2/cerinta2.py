from sklearn.impute import SimpleImputer
import numpy as np

# FUNCTIE PENTRU TRATAREA VALORILOR EXTREME
def treatOutliers(column, df):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = (df[column] < lower_bound) | (df[column] > upper_bound) # LIMITE
    df.loc[outliers, column] = np.nan  # VALOAREA ESTE OTLIER => O CONSIDERAM LIPSA

def preProcessingData(df):
    # DATE LIPSA PENTRU UN ATRIBUT INTR-UN ESANTION
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
    categorical_cols = df.select_dtypes(include=['object', 'category', 'bool']).columns

    # TRATARE OTLIERS
    for col in numeric_cols:
        treatOutliers(col, df)

    # IMPUTARE VALORI LIPSA CU MEDIANA
    num_imputer = SimpleImputer(strategy='median')
    df[numeric_cols] = num_imputer.fit_transform(df[numeric_cols])

    # IMPUTARE VALORI LIPSA CU VARIABILA CEA MAI FRECVENTA
    cat_imputer = SimpleImputer(strategy='most_frequent')
    df[categorical_cols] = cat_imputer.fit_transform(df[categorical_cols])

    # ATRIBUTE REDUNDANTE (PUTERNIC CORELATE)
    cor_matrix = df[numeric_cols].corr().abs()
    upper = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(bool))
    # SALVAM DOAR JUMATATEA SUPERIOARA A MATRICII, NU VERIFICAM DE 2 ORI 

    # ELIMINAM COLOANELE CU CORELATIE > 0.9
    redundant_cols = [col for col in upper.columns if any(upper[col] > 0.9)]
    df.drop(columns=redundant_cols, inplace=True)
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns # ACTUALIZARE LISTA


    print("Atribute eliminate din cauza corelatiei mari:", redundant_cols)

    # PLAJE VALORICE DE MARIMI DIFERITE PENTRU ATRIBUTELE NUMERICE
    from sklearn.preprocessing import StandardScaler

    scaler = StandardScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    return df