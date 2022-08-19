import os
from enum import Enum
from fastapi import FastAPI, Request, HTTPException, APIRouter
from typing import Union
from pydantic import BaseModel
from src_files.utils import get_image


from detector import analyze_image
from dotenv import load_dotenv

load_dotenv()


app = FastAPI()


class Language(str, Enum):
    es = "es"
    en = "en"


class Item(BaseModel):
    url: str
    lang: Union[Language, None] = Language.en


@app.post('/classify-image')
def process_image(request: Request, item: Item):

    try:
        image = get_image(item.url)
    except:
        raise HTTPException(status_code=400, detail="Invalid provided URL")

    response = analyze_image(image)

    response = [label[item.lang.value] for label in response]

    return {'classes': response}
