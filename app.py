from fastapi import FastAPI
from io import BytesIO
import base64
import asyncio
import uvicorn
import object_detect
from starlette.requests import Request

app = FastAPI()


@app.get("/test/")
async def test(req: Request):
    print('hello')
    print(req)


@app.post("/api/object-detect")
async def detect(request: Request):
    data = await request.json()
    b64code = data['image']
    if b64code:
        img = BytesIO(base64.b64decode(b64code))
        pred = object_detect.predict(img)
        for item in pred:
            item['score'] = float(item['score'])
        return {
            'ok': True,
            'data': pred
        }
    else:
        return {
            'ok': False,
            'data': None
        }

if __name__ == '__main__':
    uvicorn.run('app:app', host='0.0.0.0', port=8000, log_level='info')
