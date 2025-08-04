from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, FileResponse

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def index_page(request: Request):
    return """
    <html>
        <head><title>CADinfra</title></head>
        <body style="font-family: Arial; padding: 40px;">
            <h1>🚀 CADinfra 시스템</h1>
            <p>아래 기능을 선택하세요:</p>
            <ul>
                <li><a href="/auth/login">🔐 로그인</a></li>
                <li><a href="/auth/register">📝 회원가입</a></li>
                <li><a href="/download">⬇️ 다운로드</a></li>
            </ul>
        </body>
    </html>
    """


@router.get("/download", response_class=HTMLResponse)
async def download_page(request: Request):
    return """
    <html>
        <head><title>다운로드</title></head>
        <body style="font-family: Arial; padding: 40px;">
            <h2>⬇️ CADinfra 프로그램 다운로드</h2>
            <p>아래 링크를 클릭하여 최신 설치 파일을 다운로드하세요.</p>
            <a href="/static/main.exe" download>✅ main.exe 다운로드</a>
        </body>
    </html>
    """
