from fastapi import FastAPI
from router import router
from univ3 import liquidity_router
from settings import settings

app = FastAPI(title="Oracle Api", openapi_url=settings.openapi_url)

app.include_router(prefix="/api/v1", tags=['Endpoints'], router=router)
app.include_router(prefix="/api/v2", tags=['Endpoint'], router=liquidity_router)