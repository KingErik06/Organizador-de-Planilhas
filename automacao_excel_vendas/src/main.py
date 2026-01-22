from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_DIR = BASE_DIR / "data" / "input"
OUTPUT_DIR = BASE_DIR / "data" / "output"

COLUMN_MAPPING = {
    "data venda": "Data",
    "Cliente Nome": "Cliente",
    "VALOR total": "Valor",
    "produto": "Produto"
}


def load_spreadsheet(path: Path) -> pd.DataFrame:
    """Carrega a planilha Excel de entrada."""
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}.")
    return pd.read_excel(path)


def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Padroniza o nome das colunas do DataFrame."""
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace("_", " ")
    )
    return df.rename(columns=COLUMN_MAPPING)


def save_spreadsheet(df: pd.DataFrame, path: Path) -> None:
    """Salva a planilha organizada."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    df.to_excel(path, index=False)


def main():
    input_file = INPUT_DIR / "vendas_raw.xlsx"
    output_file = OUTPUT_DIR / "vendas_limpa.xlsx"
    
    df = load_spreadsheet(input_file)
    df = standardize_columns(df)
    save_spreadsheet(df, output_file)


if __name__ == "__main__":
    main()