# system/log_writer.py - 로그 기록 유틸리티

import os
from datetime import datetime

LOG_FILE = "cadinfra.log"

def write_log(message: str):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    log_message = f"{timestamp} {message}\n"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_message)
