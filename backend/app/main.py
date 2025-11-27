from fastapi import FastAPI
from app.api.routes import assets
from app.database import engine
from app.models import asset

asset.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Asset Tracker API")

app.include_router(assets.router, prefix="/api/assets", tags=["assets"])

@app.get("/")
def root():
    return {"message": "Asset Tracker API is running"}

