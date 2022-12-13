from typing import List, Literal, Optional, Union, Dict

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
        
class AnyBridgeSchemaOut(BaseModel):
    protocol_name: str = Field(alias='protocolName')
    token_name: str = Field(alias='tokenName')
    pair_address: str = Field(alias='pair_address')
    token_0: str = Field(alias='token0')
    token_1: str = Field(alias='token1')
    token_0_supply: str = Field(alias='token0Supply')
    token_1_supply: str = Field(alias='token1Supply')
    date_updated: str = Field(alias='dateUpdated')

    class Config:
        allow_population_by_field_name = True


class SwapEthereumSchemaOut(PairSchemaOut):
    protocol_name: Literal['uniswapv2', 'sushiswap'] = Field(default='uniswapv2', alias='protocolName')


class SwapPolygonSchemaOut(PairSchemaOut):
    protocol_name: Literal['quickswap'] = Field(default='quickswap', alias='protocolName')


class SwapBscSchemaOut(PairSchemaOut):
    protocol_name: Literal['pancakeswap'] = Field(default='pancakeswap', alias='protocolName')


class BridgeChainSchemaOut(BridgeTokenSchemaOut):
    protocol_name: Literal['multichain'] = Field(default='multichain', alias='protocolName')
        
        
class AnyBridgeChainSchemaOut(AnyBridgeSchemaOut):
    protocol_name: Literal['symbiosis'] = Field(default='symbiosis', alias='protocolName')


class SwapPoolsSchemaOut(BaseModel):
    ethereum: List[SwapEthereumSchemaOut]
    polygon: List[SwapPolygonSchemaOut]
    bsc: List[SwapBscSchemaOut]


class BridgePoolsSchemaOut(BaseModel):
    ethereum: List[BridgeChainSchemaOut]
    polygon: List[BridgeChainSchemaOut]
    bsc: List[BridgeChainSchemaOut]
    bsc_ethereum: List[AnyBridgeChainSchemaOut]
    polygon_ethereum: List[AnyBridgeChainSchemaOut]
    polygon_bsc: List[AnyBridgeChainSchemaOut]


class PoolsSchemaOut(BaseModel):
    swap_pools: Optional[SwapPoolsSchemaOut]
    bridge_pools: Optional[BridgePoolsSchemaOut]


class ChainGasSchemaOut(BaseModel):
    gwei: Optional[float]
    tokenPrice: Optional[float]
    date_updated: Optional[str] = Field(alias='dateUpdated')


class GasSchemaOut(BaseModel):
    ethereum: Union[ChainGasSchemaOut, float, None]
    polygon: Union[ChainGasSchemaOut, float, None]
    bsc: Union[ChainGasSchemaOut, float, None]


class QuotesSchemaOut(BaseModel):
    name: str = Field(alias='tokenName')
    value: float = Field(alias='value')

    class Config:
        allow_population_by_field_name = True


class OracleSchemaOut(BaseModel):
    pools: Optional[PoolsSchemaOut]
    gas: Optional[GasSchemaOut]
    quotes: Optional[List[QuotesSchemaOut]]


class PoolLiquiditySchemaOut(BaseModel):
    pair_name: str = Field(alias='pairName')
    token_0: str = Field(alias='token0')
    token_1: str = Field(alias='token1')
    pair_address: str = Field(alias='pairAddress')
    ticks_amount: int = Field(alias='ticksAmount')
    fi: int = Field(alias='fi')
    date_updated: Optional[str] = Field(alias='dateUpdated')
    ticks: Optional[List[Dict]] = Field(alias='ticks')

    class Config:
        allow_population_by_field_name = True
        

class LiquiditySchemaOut(BaseModel):
    liquidity: List[PoolLiquiditySchemaOut]
    
    
    