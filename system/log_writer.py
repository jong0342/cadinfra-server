# system/log_writer.py
import logging
import os

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "cadinfra.log")

os.makedirs(LOG_DIR, exist_ok=True)

# 기본 로깅 설정
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

def write_log(message: str, level: str = "info"):
    if level == "info":
        logging.info(message)
    elif level == "error":
        logging.error(message)
    elif level == "warning":
        logging.warning(message)
    else:
        logging.debug(message)
