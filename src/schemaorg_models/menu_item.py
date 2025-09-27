from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.intangible import Intangible

from schemaorg_models.demand import Demand

class MenuItem(Intangible):
    """
A food or drink item listed in a menu or menu section.
    """
    type_: Literal['https://schema.org/MenuItem'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/MenuItem'),serialization_alias='class') # type: ignore
    suitableForDiet: Optional[Union["RestrictedDiet", List["RestrictedDiet"]]] = Field(default=None,validation_alias=AliasChoices('suitableForDiet', 'https://schema.org/suitableForDiet'),serialization_alias='https://schema.org/suitableForDiet')
    menuAddOn: Optional[Union["MenuItem", List["MenuItem"], "MenuSection", List["MenuSection"]]] = Field(default=None,validation_alias=AliasChoices('menuAddOn', 'https://schema.org/menuAddOn'),serialization_alias='https://schema.org/menuAddOn')
    offers: Optional[Union[Demand, List[Demand], "Offer", List["Offer"]]] = Field(default=None,validation_alias=AliasChoices('offers', 'https://schema.org/offers'),serialization_alias='https://schema.org/offers')
    nutrition: Optional[Union["NutritionInformation", List["NutritionInformation"]]] = Field(default=None,validation_alias=AliasChoices('nutrition', 'https://schema.org/nutrition'),serialization_alias='https://schema.org/nutrition')
