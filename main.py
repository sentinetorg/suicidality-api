import uvicorn  ##ASGI
from typing import Annotated
from fastapi import FastAPI, HTTPException, status
from transformers import pipeline
from core.Token import Token

classifier = pipeline("sentiment-analysis", model="models/suicidality")
app = FastAPI(
    docs_url=None, # Disable docs (Swagger UI)
    # redoc_url=None, # Disable redoc
)


@app.get("/")
async def get_root():
    return {"status": "online"}


@app.get("/suicide/predict")
async def get_suicide_prediction(token:str, q: str | None = None):

    if not (token and Token.canLogin(token)):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect or missing `token`"
        )

    if q:
        res = classifier(q)
        return {
            "prediction": ({True: 'suicide', False: 'not-suicide'}[res[0]['label'] == 'LABEL_1']),
            "confidence": res[0]['score']
        }

    raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect or missing `q`"
        )


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=7777, reload=True)
