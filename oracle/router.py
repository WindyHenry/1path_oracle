import json
import logging

import aioredis
from fastapi import APIRouter, HTTPException

from schemas import OracleSchemaOut, QuotesSchemaOut
from typing import List
from settings import settings

router = APIRouter()

redis = aioredis.from_url(
    settings.redis_dsn,
    encoding="utf-8",
    decode_responses=True,
)

logger = logging.getLogger(__name__)


@router.get('/', response_model=OracleSchemaOut)
async def get_oracle():
    """Oracle main endpoint"""

    gas = await redis.get('gas')

    if gas:
        try:
            gas = json.loads(gas)
        except (ValueError, TypeError) as e:
            logger.error(e)
            return HTTPException(400, e)


    pools = await redis.get('pools')

    if pools:
        try:
            pools = json.loads(pools)
        except (ValueError, TypeError) as e:
            logger.error(e)
            return HTTPException(400, e)


    quotes = await redis.get('quotes')

    if quotes:
        try:
            quotes = json.loads(quotes)
        except (ValueError, TypeError) as e:
            logger.error(e)
            return HTTPException(400, e)


    data = {
        'pools': pools,
        'gas': gas,
        'quotes': quotes,
    }

    return data


@router.get('/quotes/', response_model=List[QuotesSchemaOut])
async def get_quotes():
    '''Get quotes endpoint'''

    quotes = await redis.get('quotes')

    if quotes:
        try:
            quotes = json.loads(quotes)
        except Exception as e:
            logger.error(e)
            return HTTPException(400, e)

    return quotes
