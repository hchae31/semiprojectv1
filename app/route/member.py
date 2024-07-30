from fastapi import FastAPI, APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

# 외부 라우트 설정
# 라우터 생성
member_router = APIRouter()
# 템플릿 지정
templates = Jinja2Templates(directory='views/templates')

@member_router.get("/login", response_class=HTMLResponse) # Atl+Enter
async def login(req: Request):
    return templates.TemplateResponse('member/login.html', {'request': req})

@member_router.get("/join", response_class=HTMLResponse) # Atl+Enter
async def join(req: Request):
    return templates.TemplateResponse('member/join.html', {'request': req})

@member_router.get("/myinfo", response_class=HTMLResponse) # Atl+Enter
async def myinfo(req: Request):
    return templates.TemplateResponse('member/myinfo.html', {'request': req})