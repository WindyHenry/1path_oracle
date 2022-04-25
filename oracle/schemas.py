from typing import List, Literal, Optional, Union

from pydantic import BaseModel, Field


class PairSchemaOut(BaseModel):
    protocol_name: str = Field(alias='protocolName')
    pair_name: str = Field(alias='pairName')
    token_0: Optional[str] = Field(alias='token0')
    token_1: Optional[str] = Field(alias='token1')
    token_0_supply: str = Field(alias='token0Supply')
    token_1_supply: str = Field(alias='token1Supply')
    date_updated: Optional[str] = Field(alias='dateUpdated')

    class Config:
        allow_population_by_field_name = True


class EthereumSchemaOut(PairSchemaOut):
    protocol_name: Literal['uniswapv2'] = Field(default='uniswapv2', alias='protocolName')


class PolygonSchemaOut(PairSchemaOut):
    protocol_name: Literal['quickswap'] = Field(default='quickswap', alias='protocolName')


class BscSchemaOut(PairSchemaOut):
    protocol_name: Literal['pancakeswap'] = Field(default='pancakeswap', alias='protocolName')


class PoolsSchemaOut(BaseModel):
    ethereum: List[EthereumSchemaOut]
    polygon: List[PolygonSchemaOut]
    bsc: List[BscSchemaOut]


class ChainGasSchemaOut(BaseModel):
    value: Optional[float]
    date_updated: Optional[str] = Field(alias='dateUpdated')


class GasSchemaOut(BaseModel):
    ethereum: Union[ChainGasSchemaOut, float, None]
    polygon: Union[ChainGasSchemaOut, float, None]
    bsc: Union[ChainGasSchemaOut, float, None]


class OracleSchemaOut(BaseModel):
    pools: Optional[PoolsSchemaOut]
    gas: Optional[GasSchemaOut]
