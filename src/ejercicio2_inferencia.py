import math
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# =========================
# SETTINGS
# =========================
OUTPUT_DIR = "output"
DATA_DIR   = "data"
DATA_FILE  = "student-mat.csv"

def compute_metrics(y_true, y_pred):
    mae = mean_absolute_error(y_true, y_pred)
    rmse = math.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)
    return mae, rmse, r2

if __name__ == "__main__":
    # =========================
    # CONFIGURE BASE PATHS
    # =========================
    src_folder = os.path.dirname(__file__)
    proy_folder = os.path.dirname(src_folder)
    data_file_path = os.path.join(proy_folder, DATA_DIR, DATA_FILE)
    output_folder = os.path.join(src_folder, OUTPUT_DIR)

    # =========================
    # LOADING DATA
    # =========================
    df = pd.read_csv(data_file_path, sep=";")

    # ==========================================
    # PREPROCESSING
    # ==========================================

    # GETTING TARGET VARIABLE
    y = df['G3']

    # REMOVING VARIABLES G1 G2 G3
    X = df.drop(columns=['G1', 'G2', 'G3'])

    cols_numericas = ['age', 'failures', 'absences']
    cols_ordinal = ['famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health',
                    'Medu', 'Fedu', 'traveltime', 'studytime']
    cols_categoricas = [c for c in X.columns if c not in cols_numericas+cols_ordinal]

    # ENCODING CATEGORICAL VARIABLES (One-Hot Encoding)
    # USE drop_first=True for avoiding multicollinearity
    X_encoded = pd.get_dummies(X, columns=cols_categoricas, drop_first=True)

    # ==========================================
    # PREPARING DATASET
    # ==========================================

    # DATA SPLIT
    X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

    # SCALING DATA
    scaler = StandardScaler()
    X_train[cols_numericas + cols_ordinal] = scaler.fit_transform(X_train[cols_numericas + cols_ordinal])
    X_test[cols_numericas + cols_ordinal] = scaler.transform(X_test[cols_numericas + cols_ordinal])

    # ==========================================
    # TRAINING
    # ==========================================
    model = LinearRegression()
    model.fit(X_train, y_train)

    # PREDICTIONS
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)

    # ---------------------------
    # METRICS
    # ---------------------------
    mae_train, rmse_train, r2_train = compute_metrics(y_train, y_train_pred)
    mae_test, rmse_test, r2_test = compute_metrics(y_test, y_test_pred)

    print("\n--- Métricas TRAIN ---")
    print(f"MAE: {mae_train:.3f}, RMSE: {rmse_train:.3f}, R2: {r2_train:.3f}")

    print("\n--- Métricas TEST ---")
    print(f"MAE: {mae_test:.3f}, RMSE: {rmse_test:.3f}, R2: {r2_test:.3f}")

    with open(f"{output_folder}/ej2_metricas_regresion.txt", "w") as f:
        f.write(f"MAE={mae_test:.3f}\nRMSE={rmse_test:.3f}\nR2={r2_test:.3f}")

    coef_df = pd.DataFrame({'Feature': X_train.columns, 'Coef': model.coef_})
    coef_df['Abs_Coef'] = coef_df['Coef'].abs()
    top_10 = coef_df.sort_values(by='Abs_Coef', ascending=False).head(10)
    print("\n--- Top 10 Variables Influyentes ---")
    print(top_10[['Feature', 'Coef']])

    residuals = y_test_pred - y_test.values
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test_pred, residuals, alpha=0.5, color='teal')
    plt.axhline(y=0, color='red', linestyle='--')
    plt.title('Gráfico de Residuos (Linear Regression)')
    plt.xlabel('Valores Predichos (G3)')
    plt.ylabel('Residuos')
    plt.tight_layout()
    plot_file = f"{output_folder}/ej2_residuos.png"
    plt.savefig(plot_file, dpi=150)
    plt.close()
    print(f"\n[INFO] Gráfico de residuos guardado en: {plot_file}")