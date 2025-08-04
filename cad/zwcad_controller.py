# cad/zwcad_controller.py - ZWCAD 명령어 실행 및 블럭 삽입 처리

import os
import ctypes
import win32com.client

def connect_to_zwcad():
    try:
        zwcad_app = win32com.client.Dispatch("ZWCAD.Application")
        zwcad_doc = zwcad_app.ActiveDocument
        return zwcad_app, zwcad_doc
    except Exception as e:
        return None, None

def insert_block(block_path, insert_point=(0, 0, 0)):
    zwcad_app, zwcad_doc = connect_to_zwcad()
    if zwcad_doc is None:
        return "ZWCAD 연결 실패"

    try:
        block_name = os.path.splitext(os.path.basename(block_path))[0]
        zwcad_doc.ModelSpace.InsertBlock(insert_point, block_path, 1, 1, 1, 0)
        return f"블럭 '{block_name}' 삽입 완료"
    except Exception as e:
        return f"삽입 오류: {e}"

def send_command(command):
    _, zwcad_doc = connect_to_zwcad()
    if zwcad_doc is None:
        return "ZWCAD 연결 실패"

    try:
        zwcad_doc.SendCommand(command + "\n")
        return "명령어 실행 완료"
    except Exception as e:
        return f"명령어 실행 실패: {e}"
