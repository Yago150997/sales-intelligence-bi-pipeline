import numpy as np
import pandas as pd
from datetime import datetime, timedelta

np.random.seed(42)
n_rows = 5000

# Gerar dados simulados
clientes_ids = [f"CLI-{i:04d}" for i in range(1, 401)]
produtos = {
    "Plano Starter": {"preco": 99.00, "custo": 20.00},
    "Plano Pro": {"preco": 249.00, "custo": 45.00},
    "Plano Enterprise": {"preco": 890.00, "custo": 120.00},
    "Addon Storage": {"preco": 49.00, "custo": 5.00},
}
canais = ["Google Ads", "Orgânico", "LinkedIn B2B", "Indicação", "Outbound"]

start_date = datetime(2025, 1, 1)
datas = [start_date + timedelta(days=int(np.random.randint(0, 450))) for _ in range(n_rows)]

dados = []
for i in range(n_rows):
    prod = np.random.choice(list(produtos.keys()))
    qtd = np.random.choice([1, 1, 1, 2, 3], p=[0.7, 0.15, 0.1, 0.03, 0.02])
    preco_unit = produtos[prod]["preco"]
    custo_unit = produtos[prod]["custo"]
    status = np.random.choice(["Pago", "Reembolsado", "Pendente", "Cancelado"], p=[0.82, 0.05, 0.08, 0.05])
    
    dados.append({
        "Transaction_ID": f"TRX-{100000 + i}",
        "Data_Transacao": datas[i].strftime("%Y-%m-%d"),
        "Customer_ID": np.random.choice(clientes_ids),
        "Produto": prod,
        "Quantidade": qtd,
        "Preco_Unitario": preco_unit,
        "Custo_Unitario": custo_unit,
        "Status": status,
        "Canal_Aquisicao": np.random.choice(canais),
    })

df = pd.DataFrame(dados)

# Inserir anomalias / "sujeiras" controladas para o portfólio demonstrar resolução de bugs:
# 1. Linhas duplicadas
duplicatas = df.sample(35)
df = pd.concat([df, duplicatas], ignore_index=True)

# 2. Valores nulos ou formatos corrompidos de canal
df.loc[df.sample(40).index, "Canal_Aquisicao"] = None

# 3. Preços unitários zerados ou negativos esporádicos
df.loc[df.sample(15).index, "Preco_Unitario"] = -1.0

df.to_csv("vendas_bruto.csv", index=False)
print("Arquivo 'vendas_bruto.csv' gerado com sucesso!")