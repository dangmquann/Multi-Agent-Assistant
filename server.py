# main.py
import os
from fastapi import FastAPI
from livekit import api
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/getToken")
async def get_token():
    # Lấy API key và secret từ biến môi trường
    api_key = os.getenv("LIVEKIT_API_KEY")
    api_secret = os.getenv("LIVEKIT_API_SECRET")

    if not api_key or not api_secret:
        return JSONResponse(content={"error": "Missing LIVEKIT_API_KEY or LIVEKIT_API_SECRET"}, status_code=500)

    # Tạo token
    token = api.AccessToken(api_key, api_secret) \
        .with_identity("identity") \
        .with_name("my name") \
        .with_grants(api.VideoGrants(
            room_join=True,
            room="my-room"
        ))

    return {"token": token.to_jwt()}

# Chạy ứng dụng FastAPI
# uvicorn main:app --reload
