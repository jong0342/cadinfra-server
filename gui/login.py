# gui/login.py

import tkinter as tk
from tkinter import messagebox
from gui.api import login
from gui.main_window import show_main_window

def show_login_window():
    def handle_login():
        username = entry_username.get()
        password = entry_password.get()

        try:
            token_data = login(username, password)
            print("토큰:", token_data)
            root.destroy()
            show_main_window(username)
        except Exception as e:
            messagebox.showerror("서버 오류", str(e))

    root = tk.Tk()
    root.title("CADinfra 로그인")
    root.geometry("300x180")

    tk.Label(root, text="Username").pack(pady=5)
    entry_username = tk.Entry(root)
    entry_username.pack()

    tk.Label(root, text="Password").pack(pady=5)
    entry_password = tk.Entry(root, show="*")
    entry_password.pack()

    tk.Button(root, text="Login", command=handle_login).pack(pady=15)
    root.mainloop()
