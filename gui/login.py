# gui/login.py - 로그인 창 구현

import tkinter as tk
from tkinter import messagebox
import requests
import json
import os

SERVER_URL = "http://localhost:8000"
TOKEN_FILE = "token.json"

def save_token(token: str):
    with open(TOKEN_FILE, "w") as f:
        json.dump({"token": token}, f)

def show_login_window():
    def login():
        email = email_entry.get()
        password = password_entry.get()

        if not email or not password:
            messagebox.showwarning("입력 오류", "이메일과 비밀번호를 모두 입력하세요.")
            return

        try:
            response = requests.post(
                f"{SERVER_URL}/auth/login",
                json={"email": email, "password": password}
            )
            if response.status_code == 200:
                token = response.json().get("access_token")
                save_token(token)
                messagebox.showinfo("로그인 성공", "성공적으로 로그인되었습니다.")
                window.destroy()
                from gui.main_window import show_main_window
                show_main_window()
            else:
                messagebox.showerror("로그인 실패", response.json().get("detail", "알 수 없는 오류"))
        except requests.exceptions.RequestException as e:
            messagebox.showerror("서버 오류", f"서버에 연결할 수 없습니다.\n{e}")

    def register():
        email = email_entry.get()
        password = password_entry.get()

        if not email or not password:
            messagebox.showwarning("입력 오류", "이메일과 비밀번호를 모두 입력하세요.")
            return

        try:
            response = requests.post(
                f"{SERVER_URL}/auth/register",
                json={"email": email, "password": password}
            )
            if response.status_code == 200:
                messagebox.showinfo("회원가입 성공", "회원가입이 완료되었습니다. 로그인하세요.")
            else:
                messagebox.showerror("회원가입 실패", response.json().get("detail", "알 수 없는 오류"))
        except requests.exceptions.RequestException as e:
            messagebox.showerror("서버 오류", f"서버에 연결할 수 없습니다.\n{e}")

    window = tk.Tk()
    window.title("CADinfra 로그인")
    window.geometry("320x200")

    tk.Label(window, text="이메일").pack(pady=5)
    email_entry = tk.Entry(window, width=30)
    email_entry.pack()

    tk.Label(window, text="비밀번호").pack(pady=5)
    password_entry = tk.Entry(window, show="*", width=30)
    password_entry.pack()

    tk.Button(window, text="로그인", command=login).pack(pady=10)
    tk.Button(window, text="회원가입", command=register).pack()

    window.mainloop()
