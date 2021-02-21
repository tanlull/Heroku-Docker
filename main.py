from fastapi import FastAPI
import thaiaddress
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware
import uvicorn
from decouple import config

PSID = config('PSID')

app = FastAPI()

app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)

@app.get("/")
async def main(addr : str):
    result_dict = thaiaddress.parse(addr)
    return JSONResponse(content=result_dict)

@app.get("/sendtext/")
async def sendtext(text : str):
    output = text 
    return JSONResponse(content=output)


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    uvicorn.run(app, host="0.0.0.0", port=port)

