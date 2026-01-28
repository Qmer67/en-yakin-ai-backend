from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="En Yakin AI")

app.include_router(router)
