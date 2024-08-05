from fastapi import FastAPI, Request
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from app.route.board import board_router
from app.route.member import member_router

app = FastAPI()
templates = Jinja2Templates(directory="views/templates") #jinja2 설정
app.mount('/static', StaticFiles(directory='views/static'), name='static')


# 외부 라우트 설정
app.include_router(member_router, prefix='/member')
app.include_router(board_router, prefix='/board')


@app.get("/", response_class=HTMLResponse) # Atl+Enter
async def index(req: Request):
    return templates.TemplateResponse('index.html', {'request': req})

@app.get("/join", response_class=HTMLResponse) # Atl+Enter
async def index(req: Request):
    return templates.TemplateResponse('index.html', {'request': req})

@app.get("/join", response_class=HTMLResponse) # Atl+Enter
async def index(req: Request):
    return templates.TemplateResponse('index.html', {'request': req})

@app.get("/join", response_class=HTMLResponse) # Atl+Enter
async def index(req: Request):
    return templates.TemplateResponse('index.html', {'request': req})

@member_router.get("/", response_class=HTMLResponse) # Atl+Enter
async def login(req: Request):
    return templates.TemplateResponse('member/login.html', {'request': req})

@member_router.get("/join", response_class=HTMLResponse) # Atl+Enter
async def join(req: Request):
    return templates.TemplateResponse('member.join.html', {'request': req})

@member_router.get("/myinfo", response_class=HTMLResponse) # Atl+Enter
async def myinfo(req: Request):
    return templates.TemplateResponse('member.myinfo.html', {'request': req})

@member_router.get("/list", response_class=HTMLResponse) # Atl+Enter
async def myinfo(req: Request):
    return templates.TemplateResponse('member.list.html', {'request': req})