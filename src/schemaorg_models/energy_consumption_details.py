from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.intangible import Intangible


class EnergyConsumptionDetails(Intangible):
    """
EnergyConsumptionDetails represents information related to the energy efficiency of a product that consumes energy. The information that can be provided is based on international regulations such as for example [EU directive 2017/1369](https://eur-lex.europa.eu/eli/reg/2017/1369/oj) for energy labeling and the [Energy labeling rule](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/energy-water-use-labeling-consumer) under the Energy Policy and Conservation Act (EPCA) in the US.
    """
    class_: Literal['https://schema.org/EnergyConsumptionDetails'] = Field(default='https://schema.org/EnergyConsumptionDetails', alias='@type', serialization_alias='@type') # type: ignore
    hasEnergyEfficiencyCategory: Optional[Union["EnergyEfficiencyEnumeration", List["EnergyEfficiencyEnumeration"]]] = Field(default=None, validation_alias=AliasChoices('hasEnergyEfficiencyCategory', 'https://schema.org/hasEnergyEfficiencyCategory'), serialization_alias='https://schema.org/hasEnergyEfficiencyCategory')
    energyEfficiencyScaleMax: Optional[Union["EUEnergyEfficiencyEnumeration", List["EUEnergyEfficiencyEnumeration"]]] = Field(default=None, validation_alias=AliasChoices('energyEfficiencyScaleMax', 'https://schema.org/energyEfficiencyScaleMax'), serialization_alias='https://schema.org/energyEfficiencyScaleMax')
    energyEfficiencyScaleMin: Optional[Union["EUEnergyEfficiencyEnumeration", List["EUEnergyEfficiencyEnumeration"]]] = Field(default=None, validation_alias=AliasChoices('energyEfficiencyScaleMin', 'https://schema.org/energyEfficiencyScaleMin'), serialization_alias='https://schema.org/energyEfficiencyScaleMin')
