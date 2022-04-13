from typing import List, Literal, Optional

from pydantic import BaseModel, Field


class PairSchemaOut(BaseModel):
    protocol_name: str = Field(alias='protocolName')
    pair_name: str = Field(alias='pairName')
    token_0_supply: str = Field(alias='token0Supply')
    token_1_supply: str = Field(alias='token1Supply')

    class Config:
        allow_population_by_field_name = True


class EthereumSchemaOut(PairSchemaOut):
    protocol_name: Literal['uniswapv2'] = Field(default='uniswapv2', alias='protocolName')


class PolygonSchemaOut(PairSchemaOut):
    protocol_name: Literal['quickswap'] = Field(default='quickswap', alias='protocolName')


class BscSchemaOut(PairSchemaOut):
    protocol_name: Literal['pancakeswap'] = Field(default='pancakeswap', alias='protocolName')


class PoolsSchamaOut(BaseModel):
    ethereum: List[EthereumSchemaOut]
    polygon: List[PolygonSchemaOut]
    bsc: List[BscSchemaOut]


class GasSchemaOut(BaseModel):
    ethereum: float
    polygon: float
    bsc: float


class OracleSchemaOut(BaseModel):
    pools: Optional[PoolsSchamaOut]
    gas: Optional[GasSchemaOut]
