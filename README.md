# 📊 Sales & Financial Performance Analytics | Python ETL + Power BI

Dashboard executivo focado em análise de receita, margens operacionais e eficiência de canais de aquisição para modelos de receita recorrente e serviços.

![Dashboard Preview](dashboard_screenshot.png)

## 🎯 Problema de Negócio
Empresas em crescimento frequentemente enfrentam dispersão de dados transacionais entre gateways de pagamento e planilhas, gerando:
* Duplicidade de lançamentos e dados cadastrais incompletos.
* Falta de clareza sobre o impacto de cancelamentos/reembolsos na margem líquida real.
* Dificuldade de identificar quais canais de aquisição trazem receita sustentável vs. alto custo de operação.

## 🛠️ Solução Desenvolvida
1. **Pipeline de Dados (Python / Pandas):**
   * Script automatizado de ingestão e higienização de dados brutos (`etl_pipeline.py`).
   * Deduplicação de IDs de transação e tratamento de outliers/valores inconsistentes.
   * Padronização de datas e cálculo prévio de custos unitários e receita bruta.

2. **Modelagem & Power Query (M):**
   * Construção de tabela calendário dinâmica com suporte a inteligência temporal.
   * Modelagem dimensional (*Star Schema*) garantindo integridade referencial e alta performance na engine VertiPaq.

3. **Inteligência de Negócios & DAX:**
   * Métricas dinâmicas com acompanhamento de metas (Target vs. Realizado).
   * Cálculo de margens líquidas reais considerando deduções e status de transação (`Pago`, `Cancelado`, `Reembolsado`).
   * Análise comparativa de canais e produtos com visão mensal de sazonalidade.

## 📈 Principais Insights Gerados
* **Concentração de Receita:** Identificação de que o *Plano Enterprise* responde pela maior fatia de faturamento com margem superior a 86%.
* **Eficiência de Canais:** Canais *Outbound* e *Orgânico* lideram em volume financeiro, enquanto vendas diretas não rastreadas foram isoladas para saneamento cadastral.
* **Margem vs. Metas:** Acompanhamento visual de desvios nas taxas de cancelamento com alertas condicionais.

## 💻 Como Reproduzir
```bash
# Clone o repositório
git clone [https://github.com/seu-usuario/powerbi-revenue-analytics.git](https://github.com/seu-usuario/powerbi-revenue-analytics.git)

# Execute o pipeline
python etl_pipeline.py
