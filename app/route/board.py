from fastapi import APIRouter,Request
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates


# 라우터 생성
board_router = APIRouter()
# 템플릿 지정
templates = Jinja2Templates(directory='views/templates')

@board_router.get("/write", response_class=HTMLResponse) # Atl+Enter
async def write(req: Request):
    return templates.TemplateResponse('board/write.html', {'request': req})

@board_router.get("/list", response_class=HTMLResponse) # Atl+Enter
async def write(req: Request):
    return templates.TemplateResponse('board/list.html', {'request': req})

@board_router.get("/view", response_class=HTMLResponse) # Atl+Enter
async def write(req: Request):
    return templates.TemplateResponse('board/view.html', {'request': req})

@board_router.get("/remove", response_class=HTMLResponse) # Atl+Enter
async def write(req: Request):
    return templates.TemplateResponse('board/list.html', {'request': req})

@board_router.get("/modify", response_class=HTMLResponse) # Atl+Enter
async def write(req: Request):
    return templates.TemplateResponse('board/modify.html', {'request': req})