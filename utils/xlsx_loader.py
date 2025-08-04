# utils/xlsx_loader.py - Excel 파일 로더 및 시트 파서

import pandas as pd

def load_excel_file(filepath):
    try:
        excel_data = pd.ExcelFile(filepath)
        return excel_data
    except Exception as e:
        return None

def load_excel_sheet(filepath, sheet_name):
    try:
        df = pd.read_excel(filepath, sheet_name=sheet_name, header=None)
        return df
    except Exception as e:
        return None
