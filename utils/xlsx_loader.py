# utils/xlsx_loader.py
import pandas as pd

def load_excel_sheet(file_path, sheet_name=None):
    try:
        xls = pd.ExcelFile(file_path)
        if sheet_name is None:
            sheet_name = xls.sheet_names[0]
        df = xls.parse(sheet_name=sheet_name, header=None)
        df.fillna("", inplace=True)
        return df
    except Exception as e:
        print(f"❌ 엑셀 파일 로딩 오류: {e}")
        return None
