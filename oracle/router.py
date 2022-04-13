import json
import logging

import aioredis
from fastapi import APIRouter
from schemas import OracleSchemaOut
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
        except TypeError as e:
            logger.error(e)

    data = {
        'pools': {
            'ethereum': [
                {
                    'protocol_name': 'uniswapv2',
                    'pair_name': 'mock',
                    'token_0_supply': 'mock',
                    'token_1_supply': 'mock',
                },
                {
                    'protocol_name': 'uniswapv2',
                    'pair_name': 'mock',
                    'token_0_supply': 'mock',
                    'token_1_supply': 'mock',
                },
            ],
            'polygon': [
                {
                    'protocol_name': 'quickswap',
                    'pair_name': 'mock',
                    'token_0_supply': 'mock',
                    'token_1_supply': 'mock',
                },
                {
                    'protocol_name': 'quickswap',
                    'pair_name': 'mock',
                    'token_0_supply': 'mock',
                    'token_1_supply': 'mock',
                },
            ],
            'bsc': [{
                'protocol_name': 'pancakeswap',
                'pair_name': 'mock',
                'token_0_supply': 'mock',
                'token_1_supply': 'mock',
            }, ],
        },
        'gas': gas,
    }

    return data
