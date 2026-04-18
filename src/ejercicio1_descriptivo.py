import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import seaborn as sns


# =========================
# SETTINGS
# =========================
OUTPUT_DIR = "output"
DATA_DIR   = "data"
DATA_FILE  = "student-mat.csv"

def show_structural_summary(df):
    """
        Muestra un resumen estructural básico de un DataFrame de pandas.

        Este resumen incluye:
        - Dimensiones del DataFrame (número de filas y columnas).
        - Tamaño total en memoria, expresado en bytes y megabytes.
        - Tipos de datos (dtypes) de cada columna.
        - Porcentaje de valores nulos por columna.

        Parámetros
        ----------
        df : pandas.DataFrame
            DataFrame del cual se desea obtener el resumen estructural.

        Retorna
        -------
        None
            Esta función no devuelve ningún valor. Imprime la información directamente por consola.

        Notas
        -----
        - El cálculo de memoria utiliza `memory_usage(deep=True)`, lo que incluye
          el consumo real de columnas tipo objeto (por ejemplo, strings).
        - El porcentaje de valores nulos se calcula como:
            (nulos por columna / total de filas) * 100
    """
    # Número de filas, columnas
    print("Shape:", df.shape)

    # Tamaño en memoria
    mem_bytes = df.memory_usage(deep=True).sum()
    mem_mb = mem_bytes / (1024 ** 2)
    print(f"Memoria: {mem_bytes} bytes ({mem_mb:.2f} MB)")

    # Tipos de dato de cada columna (dtypes).
    print("\nDtypes:\n", df.dtypes)

    # Valores nulos
    nulls = df.isnull().mean() * 100
    print("\n% Nulos:\n", nulls)

if __name__ == "__main__":
    # =========================
    # CONFIGURE BASE PATHS
    # =========================
    src_folder = os.path.dirname(__file__)
    proy_folder = os.path.dirname(src_folder)
    data_file_path = os.path.join(proy_folder, DATA_DIR, DATA_FILE)
    output_folder = os.path.join(src_folder, OUTPUT_DIR)

    # =========================
    # COLUMNS SETTINGS
    # =========================
    num_cols = ['age', 'failures', 'absences', 'G1', 'G2', 'G3']
    cat_cols = ['Medu', 'Fedu', 'Mjob', 'Fjob', 'reason', 'guardian', 'traveltime',
                'studytime', 'famrel', 'Dalc', 'Walc', 'freetime', 'goout', 'health']
    bin_cols = ['school', 'sex', 'address', 'famsize', 'Pstatus', 'schoolsup', 'famsup',
                'paid', 'activities', 'nursery', 'higher', 'internet', 'romantic']

    # =========================
    # LOADING DATA
    # =========================
    df = pd.read_csv(data_file_path, sep=";")

    # =========================
    # A) RESUMEN ESTRUCTURAL
    # =========================
    show_structural_summary(df)

    # =========================
    # B) ESTADÍSTICOS DESCRIPTIVOS
    # =========================
    num_df = df.loc[:, num_cols]

    stats = pd.DataFrame({
        "media": num_df.mean(),
        "mediana": num_df.median(),
        "moda": num_df.mode().iloc[0],
        "std": num_df.std(),
        "varianza": num_df.var(),
        "mínimo": num_df.min(),
        "máximo": num_df.max(),
        "cuartil 25%": num_df.quantile(.25),
        "cuartil 50%": num_df.quantile(.5),
        "cuartil 75%": num_df.quantile(.75)
    })

    print(stats)
    stats.to_csv(f"{output_folder}/ej1_descriptivo.csv")

    Q1 = df["G3"].quantile(0.25)
    Q3 = df["G3"].quantile(0.75)
    IQR = Q3 - Q1

    # IQR, Skewness y curtosis
    print(f"IQR G3: {IQR}")
    print(f"Skewness G3: {df["G3"].skew()}")
    print(f"Curtosis G3: {df["G3"].kurtosis()}")

    # C) HISTOGRAMAS
    # =========================
    df[num_cols].hist(figsize=(15, 10))
    plt.tight_layout()
    plt.savefig(f"{output_folder}/ej1_histogramas.png")
    plt.close()

    # =========================
    # BOXPLOTS (G3 vs categóricas)
    # =========================
    categorical = df.loc[:, cat_cols].columns

    n_cols = 3
    n_rows = int(np.ceil(len(categorical) / n_cols))

    plt.figure(figsize=(15, 5 * n_rows))

    for i, col in enumerate(categorical):
        plt.subplot(n_rows, n_cols, i + 1)
        sns.boxplot(x=col, y="G3", data=df)
        plt.xticks(rotation=45)

    plt.tight_layout()
    plt.savefig(f"{output_folder}/ej1_boxplots.png")
    plt.close()

    # =========================
    # OUTLIERS (IQR METHOD)
    # =========================
    outliers_info = {}

    for col in num_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1

        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        outliers = df[(df[col] < lower) | (df[col] > upper)]
        if len(outliers):
            outliers_info[col] = len(outliers)
            print ('*'*100 + f"\n{col} - Lower bound: {lower} - Upper bound: {upper} \n" + '*'*100)
            print (outliers.to_string())

    print("\nOutliers por columna:\n", outliers_info)

    # =========================
    # D) VARIABLES CATEGÓRICAS
    # =========================
    plt.figure(figsize=(15, 5 * n_rows))

    for i, col in enumerate(cat_cols):
        plt.subplot(n_rows, n_cols, i + 1)
        df[col].value_counts().plot(kind="bar")
        plt.title(col)

    plt.tight_layout()
    plt.savefig(f"{output_folder}/ej1_categoricas.png")
    plt.close()

    # Frecuencia absoluta y relativa
    print('*'*100)
    print("Análisis de las frecuencias de las variables categóricas")
    print('*'*100)
    for col in cat_cols + bin_cols:
        freq_abs = df[col].value_counts()
        freq_rel = df[col].value_counts(normalize=True)

        tabla_frec = pd.concat([freq_abs, freq_rel], axis=1)
        tabla_frec.columns = ['Frec. Absoluta', 'Frec. Relativa (%)']

        print(f"\n--- Análisis de la columna: {col} ---")
        print(tabla_frec)
        print("-" * 40)

    # =========================
    # E) CORRELACIONES
    # =========================
    corr = df[num_cols].corr()

    plt.figure(figsize=(12, 10))
    sns.heatmap(corr, annot=False, cmap="coolwarm")
    plt.title("Heatmap correlación")
    plt.savefig(f"{output_folder}/ej1_heatmap_correlacion.png")
    plt.close()

    # Top corr con G3
    corr_target = corr["G3"].abs().sort_values(ascending=False)
    print("\nTop correlaciones con G3:\n", corr_target.head(5))

    # Multicolinealidad
    high_corr_pairs = []

    for i in range(len(corr.columns)):
        for j in range(i):
            if abs(corr.iloc[i, j]) > 0.9:
                high_corr_pairs.append((corr.columns[i], corr.columns[j], corr.iloc[i, j]))

    print("\nPares con alta correlación (>0.9):\n", high_corr_pairs)

    print("Todos los ficheros fueron generados. FIN :-)")