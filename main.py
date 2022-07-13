from enum import Enum
from fastapi import FastAPI, Request, HTTPException
from typing import Union
from pydantic import BaseModel
from src_files.utils.utils import get_image
from detector import analyze_image


class Language(str, Enum):
    es = "es"
    en = "en"


class Item(BaseModel):
    url: str
    lang: Union[Language, None] = Language.en


app = FastAPI()


@app.post('/api/process-image')
def process_image(request: Request, item: Item):
    try:
        image = get_image(item.url)
    except:
        raise HTTPException(status_code=400, detail="Invalid URL provided")

    response = analyze_image(image)

    response = [label[item.lang.value] for label in response]

    return {'classes': response}
