# gui/login.py
import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json
import os

API_URL = "http://localhost:8000/auth"
TOKEN_FILE = "token.json"
CONFIG_FILE = "user_config.json"

def show_login_window():
    login_win = tk.Tk()
    login_win.title("CADinfra 로그인")
    login_win.geometry("400x300")
    login_win.resizable(False, False)

    email_var = tk.StringVar()
    pw_var = tk.StringVar()
    remember_var = tk.BooleanVar()
    auto_login_var = tk.BooleanVar()

    # 설정 불러오기
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            config = json.load(f)
            email_var.set(config.get("saved_email", ""))
            remember_var.set(config.get("remember_email", False))
            auto_login_var.set(config.get("auto_login", False))

    def save_config():
        config = {
            "saved_email": email_var.get() if remember_var.get() else "",
            "remember_email": remember_var.get(),
            "auto_login": auto_login_var.get()
        }
        with open(CONFIG_FILE, "w") as f:
            json.dump(config, f)

    def try_login():
        email = email_var.get().strip()
        pw = pw_var.get().strip()
        if not email or not pw:
            messagebox.showwarning("입력 오류", "이메일과 비밀번호를 모두 입력하세요.")
            return
        try:
            response = requests.post(f"{API_URL}/login", json={"email": email, "password": pw})
            if response.status_code == 200:
                token = response.json()["access_token"]
                with open(TOKEN_FILE, "w") as f:
                    json.dump({"token": token}, f)
                save_config()
                login_win.destroy()
                from gui.main_window import run_main_gui
                run_main_gui(token)
            else:
                messagebox.showerror("로그인 실패", response.json().get("detail", "오류 발생"))
        except Exception as e:
            messagebox.showerror("오류", f"서버 연결 실패: {e}")

    def register():
        email = email_var.get().strip()
        pw = pw_var.get().strip()
        if not email or not pw:
            messagebox.showwarning("입력 오류", "이메일과 비밀번호를 입력해야 합니다.")
            return
        try:
            response = requests.post(f"{API_URL}/register", json={"email": email, "password": pw})
            if response.status_code == 200:
                messagebox.showinfo("회원가입 완료", "성공적으로 회원가입 되었습니다. 로그인해주세요.")
            else:
                messagebox.showerror("회원가입 실패", response.json().get("detail", "오류 발생"))
        except Exception as e:
            messagebox.showerror("오류", f"서버 연결 실패: {e}")

    # 자동 로그인
    if auto_login_var.get() and email_var.get():
        try_login()
        return

    ttk.Label(login_win, text="이메일:").pack(pady=(20, 0))
    email_entry = ttk.Entry(login_win, textvariable=email_var)
    email_entry.pack()

    ttk.Label(login_win, text="비밀번호:").pack(pady=(10, 0))
    pw_entry = ttk.Entry(login_win, textvariable=pw_var, show="*")
    pw_entry.pack()

    options_frame = ttk.Frame(login_win)
    options_frame.pack(pady=10)
    ttk.Checkbutton(options_frame, text="아이디 저장", variable=remember_var).pack(side=tk.LEFT, padx=5)
    ttk.Checkbutton(options_frame, text="자동 로그인", variable=auto_login_var).pack(side=tk.LEFT, padx=5)

    btn_frame = ttk.Frame(login_win)
    btn_frame.pack(pady=10)
    ttk.Button(btn_frame, text="로그인", command=try_login).pack(side=tk.LEFT, padx=10)
    ttk.Button(btn_frame, text="회원가입", command=register).pack(side=tk.LEFT, padx=10)

    login_win.mainloop()
