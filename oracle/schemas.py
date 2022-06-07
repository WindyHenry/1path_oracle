from typing import List, Literal, Optional, Union

from pydantic import BaseModel, Field


class PairSchemaOut(BaseModel):
    protocol_name: str = Field(alias='protocolName')
    pair_name: str = Field(alias='pairName')
    token_0: Optional[str] = Field(alias='token0')
    token_1: Optional[str] = Field(alias='token1')
    pair_address: Optional[str] = Field(alias='pairAddress')
    token_0_supply: str = Field(alias='token0Supply')
    token_1_supply: str = Field(alias='token1Supply')
    date_updated: Optional[str] = Field(alias='dateUpdated')

    class Config:
        allow_population_by_field_name = True


class BridgeTokenSchemaOut(BaseModel):
    protocol_name: str = Field(alias='protocolName')
    token_name: str = Field(alias='tokenName')
    token_address: str = Field(alias='tokenAddress')
    token_supply: str = Field(alias='tokenSupply')
    date_updated: str = Field(alias='dateUpdated')

    class Config:
        allow_population_by_field_name = True


class SwapEthereumSchemaOut(PairSchemaOut):
    protocol_name: Literal['uniswapv2'] = Field(default='uniswapv2', alias='protocolName')


class SwapPolygonSchemaOut(PairSchemaOut):
    protocol_name: Literal['quickswap'] = Field(default='quickswap', alias='protocolName')


class SwapBscSchemaOut(PairSchemaOut):
    protocol_name: Literal['pancakeswap'] = Field(default='pancakeswap', alias='protocolName')


class BridgeChainSchemaOut(BridgeTokenSchemaOut):
    protocol_name: Literal['multichain'] = Field(default='multichain', alias='protocolName')


class SwapPoolsSchemaOut(BaseModel):
    ethereum: List[SwapEthereumSchemaOut]
    polygon: List[SwapPolygonSchemaOut]
    bsc: List[SwapBscSchemaOut]


class BridgePoolsSchemaOut(BaseModel):
    ethereum: List[BridgeChainSchemaOut]
    polygon: List[BridgeChainSchemaOut]
    bsc: List[BridgeChainSchemaOut]


class PoolsSchemaOut(BaseModel):
    swap_pools: Optional[SwapPoolsSchemaOut]
    bridge_pools: Optional[BridgePoolsSchemaOut]


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
