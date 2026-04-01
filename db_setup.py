import duckdb
import pandas as pd

def load_data(file_path):
    conn = duckdb.connect(database=':memory:')

    # Load sheets
    xls = pd.ExcelFile(file_path)

    for sheet in xls.sheet_names:
        df = xls.parse(sheet)
        table_name = sheet.strip().lower().replace(" ", "_")
        conn.register(table_name, df)

    return conn