from fastapi import (
    APIRouter,
    Request,
    Form,
    HTTPException
)

from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from app.schemas import PromptRequest

router = APIRouter()

templates = Jinja2Templates(
    directory="app/templates"
)


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request
        }
    )


@router.post("/generate")
async def generate_comic(
    request: Request,
    story_prompt: str = Form(...),
    character_name: str = Form(...),
    setting: str = Form(...),
    tone: str = Form(...),
    art_style: str = Form(...)
):

    try:

        # Placeholder
        layout = []
        pdf_path = ""

        return templates.TemplateResponse(
            "comic_preview.html",
            {
                "request": request,
                "layout": layout,
                "pdf_path": pdf_path
            }
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.post("/generate-comic/json")
async def generate_comic_json(
    payload: PromptRequest
):

    try:

        return {
            "message": "Comic generation endpoint ready",
            "data": payload.dict()
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.get("/export-success")
async def export_success(
    request: Request
):

    return templates.TemplateResponse(
        "export_success.html",
        {
            "request": request
        }
    )


@router.get("/test-image")
async def test_image():

    return {
        "message": "Image generation route ready"
    }