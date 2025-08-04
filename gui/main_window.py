# gui/main_window.py - CADinfra 메인 GUI 창 구현

import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import pandas as pd
from system.log_writer import write_log
from utils.xlsx_loader import load_excel_sheets, load_sheet_data

selected_file = None
selected_sheet = None
sheet_data = None

def show_main_window():
    def open_excel_file():
        global selected_file
        file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
        if file_path:
            selected_file = file_path
            sheet_list = load_excel_sheets(file_path)
            sheet_listbox.delete(0, tk.END)
            for sheet in sheet_list:
                sheet_listbox.insert(tk.END, sheet)
            write_log("엑셀 파일 열기", f"{file_path} 선택됨")

    def on_sheet_select(event):
        global selected_sheet, sheet_data
        selection = sheet_listbox.curselection()
        if selection:
            selected_sheet = sheet_listbox.get(selection[0])
            sheet_data = load_sheet_data(selected_file, selected_sheet)
            update_treeview(sheet_data)
            write_log("시트 선택", f"{selected_sheet} 미리보기 로드")

    def update_treeview(df):
        tree.delete(*tree.get_children())
        tree["columns"] = list(df.columns)
        tree["show"] = "headings"
        for col in df.columns:
            tree.heading(col, text=col)
            tree.column(col, width=80, anchor='center')
        for _, row in df.iterrows():
            tree.insert("", "end", values=list(row))

    def execute_cad_commands():
        if sheet_data is None:
            messagebox.showwarning("경고", "시트를 먼저 선택해주세요.")
            return
        try:
            # 실제 CAD 연동 기능은 추후 구현
            write_log("CAD 명령어 실행", f"{selected_sheet} 기반 작업 실행됨")
            messagebox.showinfo("성공", "CAD 명령어가 실행되었습니다. (모의 실행)")
        except Exception as e:
            write_log("오류", f"CAD 명령어 실행 중 오류 발생: {str(e)}")
            messagebox.showerror("실패", f"오류 발생: {str(e)}")

    # GUI 구성
    root = tk.Tk()
    root.title("CADinfra 메인")
    root.geometry("800x600")

    top_frame = tk.Frame(root)
    top_frame.pack(pady=10)

    tk.Button(top_frame, text="엑셀 파일 열기", command=open_excel_file).pack(side=tk.LEFT, padx=5)
    tk.Button(top_frame, text="CAD 명령어 전개", command=execute_cad_commands).pack(side=tk.LEFT, padx=5)

    mid_frame = tk.Frame(root)
    mid_frame.pack(fill=tk.BOTH, expand=True)

    sheet_listbox = tk.Listbox(mid_frame, height=10, width=25)
    sheet_listbox.pack(side=tk.LEFT, padx=10, pady=10)
    sheet_listbox.bind("<<ListboxSelect>>", on_sheet_select)

    tree = ttk.Treeview(mid_frame)
    tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    root.mainloop()
