from fastapi import FastAPI
from io import BytesIO
import base64
import uvicorn
import object_detect
from starlette.requests import Request

app = FastAPI()


@app.get('/')
async def root():
    return {1: 1}

@app.post("/api/object-detect")
async def detect(request: Request):
    data = await request.json()
    b64code = data['image']
    if b64code:
        img = BytesIO(base64.b64decode(b64code))
        pred = object_detect.predict(img)
        res = set(i['cls'] for i in pred)
        return {
            'ok': True,
            'data': list(res)
        }
    else:
        return {
            'ok': False,
            'data': None
        }

if __name__ == '__main__':
    uvicorn.run('app:app', host='0.0.0.0', port=8000, log_level='info')
