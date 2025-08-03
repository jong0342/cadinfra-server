# gui/main_window.py
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import os
import logging

excel_file = None
excel_data = None

def run_main_gui(token: str = ""):
    root = tk.Tk()
    root.title("CADinfra 메인")
    root.geometry("1100x700")
    root.iconbitmap(default=os.path.join("assets", "cadinfralogo.ico"))

    notebook = ttk.Notebook(root)
    notebook.pack(fill=tk.BOTH, expand=True)

    main_tab = ttk.Frame(notebook)
    notebook.add(main_tab, text="📁 전개도 시트 선택")

    # 시트 선택
    sheet_frame = ttk.LabelFrame(main_tab, text="엑셀 시트 선택")
    sheet_frame.pack(fill=tk.X, padx=10, pady=5)

    sheet_listbox = tk.Listbox(sheet_frame, height=4, exportselection=False)
    sheet_listbox.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(10, 0), pady=5)

    sheet_scroll = tk.Scrollbar(sheet_frame, orient="vertical", command=sheet_listbox.yview)
    sheet_scroll.pack(side=tk.RIGHT, fill=tk.Y)
    sheet_listbox.config(yscrollcommand=sheet_scroll.set)

    # 미리보기
    preview_frame = ttk.LabelFrame(main_tab, text="시트 미리보기")
    preview_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

    tree = ttk.Treeview(preview_frame, show="headings")
    tree.pack(fill=tk.BOTH, expand=True)

    # 로그 출력
    log_frame = ttk.LabelFrame(root, text="로그 출력")
    log_frame.pack(fill=tk.X, padx=10, pady=5)

    log_output = tk.Text(log_frame, height=8)
    log_output.pack(fill=tk.X, padx=5, pady=5)

    def log(msg):
        logging.info(msg)
        log_output.insert(tk.END, msg + "\n")
        log_output.see(tk.END)

    def resize_treeview():
        tree.update()
        total_width = tree.winfo_width()
        num_columns = len(tree["columns"])
        if num_columns:
            col_width = max(int(total_width / num_columns), 80)
            for col in tree["columns"]:
                tree.column(col, width=col_width)

    def select_excel():
        global excel_file
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
        if file_path:
            try:
                excel_file = pd.ExcelFile(file_path)
                sheet_listbox.delete(0, tk.END)
                for name in excel_file.sheet_names:
                    sheet_listbox.insert(tk.END, name)
                log(f"✅ 파일 불러오기 완료: {os.path.basename(file_path)}")
            except Exception as e:
                log(f"❌ 파일 불러오기 실패: {e}")

    def on_sheet_select(event):
        global excel_data
        selection = sheet_listbox.curselection()
        if selection:
            selected_sheet = sheet_listbox.get(selection[0])
            try:
                df = excel_file.parse(sheet_name=selected_sheet, header=None)
                df.fillna("", inplace=True)
                excel_data = df

                tree.delete(*tree.get_children())
                tree["columns"] = list(range(len(df.columns)))
                for col in tree["columns"]:
                    tree.heading(col, text=str(col + 1))
                    tree.column(col, width=100, anchor="center")

                for _, row in df.iterrows():
                    tree.insert("", "end", values=list(row))

                resize_treeview()
                log(f"📄 시트 미리보기: {selected_sheet}")
            except Exception as e:
                log(f"❌ 시트 로딩 실패: {e}")

    def generate_cad_commands():
        if excel_data is None:
            log("⚠️ 시트를 먼저 선택하세요.")
            return
        try:
            log("🚧 CAD 명령어 전개 시작...")
            log("✅ CAD 명령어 전개 완료 (예시)")
        except Exception as e:
            log(f"❌ CAD 명령어 전개 오류: {e}")

    # 버튼
    top_btn_frame = ttk.Frame(root)
    top_btn_frame.pack(fill=tk.X, padx=10, pady=5)

    ttk.Button(top_btn_frame, text="📂 엑셀 파일 열기", command=select_excel).pack(side=tk.LEFT, padx=(0, 5))
    ttk.Button(top_btn_frame, text="🛠️ CAD 명령어 전개", command=generate_cad_commands).pack(side=tk.LEFT)

    sheet_listbox.bind("<<ListboxSelect>>", on_sheet_select)

    root.mainloop()
