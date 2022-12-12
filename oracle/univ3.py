import json
import logging

import aioredis
from fastapi import APIRouter

from schemas import LiquiditySchemaOut
from settings import settings

liquidity_router = APIRouter()

redis = aioredis.from_url(
    settings.redis_dsn,
    encoding="utf-8",
    decode_responses=True,
)

logger = logging.getLogger(__name__)


@liquidity_router.get('/', response_model=LiquiditySchemaOut)
async def get_liq():
    """Liquidity main endpoint"""

    liq = await redis.get('liquidity')

    
    if liq:
        try:
            liq = json.loads(liq)
        except (ValueError, TypeError) as e:
            logger.error(e)

    

    return {"liquidity": liq}
