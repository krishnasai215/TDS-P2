from app import app
from fastapi.responses import JSONResponse

# Vercel's Python runtime looks for 'app' in this file
# This ensures FastAPI runs as ASGI
# You don't run uvicorn here; Vercel does it automatically.
