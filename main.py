import pandas as pd
import schedule
import time
from datetime import datetime
import os

# Caminhos dos arquivos
DATA_RAW = os.path.join("data", "raw_data.csv")
DATA_PROCESSED = os.path.join("data", "processed_data.csv")

def process_data():
    """Lê raw_data.csv, processa e salva processed_data.csv"""
    try:
        print(f"[{datetime.now()}] Iniciando processamento...")
        df = pd.read_csv(DATA_RAW, parse_dates=["Data"])

        # Validação de colunas
        expected_cols = {"Data", "Produto", "Quantidade", "PrecoUnitario"}
        if not expected_cols.issubset(set(df.columns)):
            raise ValueError(f"Colunas esperadas: {expected_cols}. Encontradas: {set(df.columns)}")

        # Cria coluna de receita por linha
        df["Receita"] = df["Quantidade"] * df["PrecoUnitario"]

        # Agrupa por produto
        df_summary = (
            df.groupby("Produto")
            .agg({
                "Quantidade": "sum",
                "Receita": "sum",
                "PrecoUnitario": "mean"
            })
            .reset_index()
            .rename(columns={"PrecoUnitario": "PrecoMedio"})
        )

        # Ordena por Receita decrescente
        df_summary = df_summary.sort_values("Receita", ascending=False)

        # Salva CSV pronto para Power BI
        df_summary.to_csv(DATA_PROCESSED, index=False, sep=';', lineterminator='\n')
        print(f"[{datetime.now()}] Processamento concluído. {DATA_PROCESSED} atualizado.")
    except FileNotFoundError:
        print(f"[{datetime.now()}] ERRO: arquivo {DATA_RAW} não encontrado.")
    except Exception as e:
        print(f"[{datetime.now()}] ERRO durante processamento: {e}")

def main():
    # Executa uma vez imediatamente
    process_data()

    # Agendamento para teste: a cada 1 minuto
    schedule.every(1).minutes.do(process_data)

    print("Agendador iniciado. Pressione Ctrl+C para parar.")
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nParando automação. Até mais!")

if __name__ == "__main__":
    main()
