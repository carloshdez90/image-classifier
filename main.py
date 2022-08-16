import os
from enum import Enum
from fastapi import FastAPI, Request, HTTPException, APIRouter
from typing import Union
from pydantic import BaseModel
from src_files.utils import get_image, validate_token


from detector import analyze_image
from dotenv import load_dotenv

load_dotenv()


def initialize():
    app = FastAPI()

    env_vars = {"sso_url":  os.getenv('sso_url'),
                "sso_realm": os.getenv('sso_realm'),
                "sso_key":  os.getenv('sso_key')}
    return app, env_vars


class Language(str, Enum):
    es = "es"
    en = "en"


class Item(BaseModel):
    url: str
    lang: Union[Language, None] = Language.en
    token: str


app, env_vars = initialize()


@app.post('/classify-image')
def process_image(request: Request, item: Item):

    # validate if the provided token is valid
    try:
        response = validate_token(item.token, env_vars)
    except:
        raise HTTPException(status_code=400, detail="Invalid provided token")

    if response.status_code != 200 or dict(response.json())['active'] == False:
        raise HTTPException(
            status_code=400, detail="Invalid provided token")

    try:
        image = get_image(item.url)
    except:
        raise HTTPException(status_code=400, detail="Invalid provided URL")

    response = analyze_image(image)

    response = [label[item.lang.value] for label in response]

    return {'classes': response}
