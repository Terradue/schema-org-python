from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .intangible import Intangible
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .eu_energy_efficiency_enumeration import EUEnergyEfficiencyEnumeration
    from .energy_efficiency_enumeration import EnergyEfficiencyEnumeration

class EnergyConsumptionDetails(Intangible):
    '''
    EnergyConsumptionDetails represents information related to the energy efficiency of a product that consumes energy. The information that can be provided is based on international regulations such as for example [EU directive 2017/1369](https://eur-lex.europa.eu/eli/reg/2017/1369/oj) for energy labeling and the [Energy labeling rule](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/energy-water-use-labeling-consumer) under the Energy Policy and Conservation Act (EPCA) in the US.

    Attributes:
        hasEnergyEfficiencyCategory: Defines the energy efficiency Category (which could be either a rating out of range of values or a yes/no certification) for a product according to an international energy efficiency standard.
        energyEfficiencyScaleMax: Specifies the most energy efficient class on the regulated EU energy consumption scale for the product category a product belongs to. For example, energy consumption for televisions placed on the market after January 1, 2020 is scaled from D to A+++.
        energyEfficiencyScaleMin: Specifies the least energy efficient class on the regulated EU energy consumption scale for the product category a product belongs to. For example, energy consumption for televisions placed on the market after January 1, 2020 is scaled from D to A+++.
    '''
    class_: Literal['https://schema.org/EnergyConsumptionDetails'] = Field( # type: ignore
        default='https://schema.org/EnergyConsumptionDetails',
        alias='@type',
        serialization_alias='@type'
    )
    hasEnergyEfficiencyCategory: Optional[Union['EnergyEfficiencyEnumeration', List['EnergyEfficiencyEnumeration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasEnergyEfficiencyCategory',
            'https://schema.org/hasEnergyEfficiencyCategory'
        ),
        serialization_alias='https://schema.org/hasEnergyEfficiencyCategory'
    )
    energyEfficiencyScaleMax: Optional[Union['EUEnergyEfficiencyEnumeration', List['EUEnergyEfficiencyEnumeration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'energyEfficiencyScaleMax',
            'https://schema.org/energyEfficiencyScaleMax'
        ),
        serialization_alias='https://schema.org/energyEfficiencyScaleMax'
    )
    energyEfficiencyScaleMin: Optional[Union['EUEnergyEfficiencyEnumeration', List['EUEnergyEfficiencyEnumeration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'energyEfficiencyScaleMin',
            'https://schema.org/energyEfficiencyScaleMin'
        ),
        serialization_alias='https://schema.org/energyEfficiencyScaleMin'
    )
