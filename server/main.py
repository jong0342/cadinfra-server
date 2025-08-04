from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

from server.auth import router as auth_router

app = FastAPI()

# 템플릿 설정 (templates 폴더 필요)
templates = Jinja2Templates(directory="server/templates")

# 정적 파일 (exe, 이미지 등 다운로드 링크 제공용)
app.mount("/static", StaticFiles(directory="server/static"), name="static")

# 라우터 등록
app.include_router(auth_router, prefix="/auth", tags=["auth"])


# ✅ 루트 경로 → HTML 홈페이지 렌더링
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
