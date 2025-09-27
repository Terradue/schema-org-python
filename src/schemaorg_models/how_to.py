from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work import CreativeWork

from schemaorg_models.creative_work import CreativeWork
from schemaorg_models.item_list import ItemList

class HowTo(CreativeWork):
    """
Instructions that explain how to achieve a result by performing a sequence of steps.
    """
    class_: Literal['https://schema.org/HowTo'] = Field(default='https://schema.org/HowTo', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    prepTime: Optional[Union["Duration", List["Duration"]]] = Field(default=None, validation_alias=AliasChoices('prepTime', 'https://schema.org/prepTime'), serialization_alias='https://schema.org/prepTime')
    performTime: Optional[Union["Duration", List["Duration"]]] = Field(default=None, validation_alias=AliasChoices('performTime', 'https://schema.org/performTime'), serialization_alias='https://schema.org/performTime')
    supply: Optional[Union["HowToSupply", List["HowToSupply"], str, List[str]]] = Field(default=None, validation_alias=AliasChoices('supply', 'https://schema.org/supply'), serialization_alias='https://schema.org/supply')
    totalTime: Optional[Union["Duration", List["Duration"]]] = Field(default=None, validation_alias=AliasChoices('totalTime', 'https://schema.org/totalTime'), serialization_alias='https://schema.org/totalTime')
    step: Optional[Union[str, List[str], "HowToStep", List["HowToStep"], CreativeWork, List[CreativeWork], "HowToSection", List["HowToSection"]]] = Field(default=None, validation_alias=AliasChoices('step', 'https://schema.org/step'), serialization_alias='https://schema.org/step')
    estimatedCost: Optional[Union[str, List[str], "MonetaryAmount", List["MonetaryAmount"]]] = Field(default=None, validation_alias=AliasChoices('estimatedCost', 'https://schema.org/estimatedCost'), serialization_alias='https://schema.org/estimatedCost')
    steps: Optional[Union[str, List[str], CreativeWork, List[CreativeWork], ItemList, List[ItemList]]] = Field(default=None, validation_alias=AliasChoices('steps', 'https://schema.org/steps'), serialization_alias='https://schema.org/steps')
    tool: Optional[Union[str, List[str], "HowToTool", List["HowToTool"]]] = Field(default=None, validation_alias=AliasChoices('tool', 'https://schema.org/tool'), serialization_alias='https://schema.org/tool')
    yield_: Optional[Union[str, List[str], "QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None, validation_alias=AliasChoices('yield', 'https://schema.org/yield'), serialization_alias='https://schema.org/yield')
