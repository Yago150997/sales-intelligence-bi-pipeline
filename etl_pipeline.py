import pandas as pd
import numpy as np

def run_etl(input_file="vendas_bruto.csv"):
    df = pd.read_csv(input_file)
    print(f"Total bruto: {len(df)} linhas")

    # 1. Deduplicação
    df = df.drop_duplicates(subset=["Transaction_ID"])

    # 2. Tratamento de anomalias de preço
    # Remove ou corrige transações com preço inconsistente
    df = df[df["Preco_Unitario"] > 0]

    # 3. Tratamento de nulos em canal
    df["Canal_Aquisicao"] = df["Canal_Aquisicao"].fillna("Direto / Não Identificado")

    # 4. Cálculo de colunas derivadas
    df["Data_Transacao"] = pd.to_datetime(df["Data_Transacao"])
    df["Receita_Bruta"] = df["Quantidade"] * df["Preco_Unitario"]
    df["Custo_Total"] = df["Quantidade"] * df["Custo_Unitario"]
    df["Margem_Bruta"] = df["Receita_Bruta"] - df["Custo_Total"]

    # 5. Exportar base limpa para o Power BI
    df.to_csv("fato_vendas.csv", index=False)
    print(f"Total tratado: {len(df)} linhas salvas em 'fato_vendas.csv'!")

if __name__ == "__main__":
    run_etl()